#!/usr/bin/env python3
"""Convert a narrow, selected Apple Health quantity type to private daily CSV.

No network, credentials, or database. Review the output; this is not a medical calculation.
"""
import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

TYPES = {
    'HKQuantityTypeIdentifierStepCount': ('steps', 'count', 'sum'),
    'HKQuantityTypeIdentifierRestingHeartRate': ('resting_heart_rate', 'count/min', 'mean'),
    'HKQuantityTypeIdentifierHeartRateVariabilitySDNN': ('hrv_sdnn', 'ms', 'mean'),
}


def convert(path, out, selected, chosen_source=None):
    metric, expected_unit, aggregation = TYPES[selected]
    daily = defaultdict(lambda: defaultdict(list))
    sources = set()
    skipped = 0
    # iterparse clears each record to avoid retaining a large Health export.
    for _, element in ET.iterparse(path, events=('end',)):
        if element.tag != 'Record':
            element.clear()
            continue
        if element.get('type') == selected:
            try:
                start = element.attrib['startDate']
                date = datetime.strptime(start[:10], '%Y-%m-%d').date().isoformat()
                value = float(element.attrib['value'])
                if element.get('unit') != expected_unit or not (-1e12 < value < 1e12):
                    raise ValueError('unexpected unit or value')
                source = element.get('sourceName', 'unknown')
                sources.add(source)
                daily[source][date].append(value)
            except (KeyError, ValueError):
                skipped += 1
        element.clear()
    if len(sources) > 1 and chosen_source is None:
        raise ValueError('Multiple sources found: ' + ', '.join(sorted(sources)) + '. Choose one with --source to avoid double counting.')
    if chosen_source is not None and chosen_source not in sources:
        raise ValueError('Source not found. Available: ' + ', '.join(sorted(sources)))
    source = chosen_source or next(iter(sources), 'unknown')
    selected_days = daily[source]
    with open(out, 'w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['date', 'metric', 'value', 'unit', 'source', 'context_phase'])
        for day, values in sorted(selected_days.items()):
            result = sum(values) if aggregation == 'sum' else sum(values) / len(values)
            writer.writerow([day, metric, format(result, '.8g'), expected_unit, 'Apple Health: ' + source, ''])
    return len(selected_days), skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('format', choices=['apple'])
    parser.add_argument('input', type=Path, help='Extracted Apple Health export.xml')
    parser.add_argument('output', type=Path, help='Private normalized CSV; never commit it')
    parser.add_argument('--type', choices=sorted(TYPES), required=True, help='One Apple quantity type')
    parser.add_argument('--source', help='Exact Apple Health sourceName; required when multiple sources occur')
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Input and output must differ')
    try:
        count, skipped = convert(args.input, args.output, args.type, args.source)
    except ValueError as error:
        parser.error(str(error))
    print(f'Wrote {count} daily rows; skipped {skipped} invalid matching records. Review units and coverage.')


if __name__ == '__main__':
    main()
