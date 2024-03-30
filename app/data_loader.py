import pandas as pd
import json
from .database import SessionLocal
from .models import Route, Point


def clean_json_string(s):
    # corrects json notation
    s = s.strip()
    if not s.startswith('['):
        s = '[' + s
    if not s.endswith(']'):
        s += ']'

    s = s.replace("'", '"')

    s = s.replace('] [', '], [')

    return s


def load_data(csv_file_path: str):
    session = SessionLocal()
    data = pd.read_csv(csv_file_path, dtype=str)

    for _, row in data.iterrows():
        # Skip the row if 'route_id' or 'points' is missing
        if pd.isna(row['route_id']) or pd.isna(row['points']):
            continue

        # Check if the route already exists
        existing_route = session.query(Route).filter_by(route_id=row['route_id']).first()
        if existing_route:
            print(f"Route with route_id {row['route_id']} already exists. Skipping.")
            continue

        # Create new route object
        route = Route(
            route_id=row['route_id'],
            from_port=row.get('from_port', None),
            to_port=row.get('to_port', None),
            leg_duration=row.get('leg_duration', None)
        )
        session.add(route)
        session.commit()

        # Clean and load points data
        try:
            clean_points_str = clean_json_string(row['points'])
            points_data = json.loads(clean_points_str)
            for point in points_data:
                point_obj = Point(
                    longitude=point[0],
                    latitude=point[1],
                    timestamp=point[2],
                    speed=point[3] if point[3] is not None else 0.0,
                    route_id=route.route_id
                )
                session.add(point_obj)
        except json.JSONDecodeError as e:
            print(f"JSON decode error for route_id {row['route_id']}: {e}")
            session.rollback()
            continue

        session.commit()

    print("Data has been loaded into the database.")
