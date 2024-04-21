import os
import exifread
import csv

def extract_gps(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            latitude = tags.get('GPS GPSLatitude')
            longitude = tags.get('GPS GPSLongitude')
            altitude = tags.get('GPS GPSAltitude')
            if latitude and longitude:
                # Extract latitude and longitude data
                    lat_degrees = latitude.values[0].num / latitude.values[0].den
                    lat_minutes = latitude.values[1].num / latitude.values[1].den
                    lat_seconds = latitude.values[2].num / latitude.values[2].den
                    lng_degrees = longitude.values[0].num / longitude.values[0].den
                    lng_minutes = longitude.values[1].num / longitude.values[1].den
                    lng_seconds = longitude.values[2].num / longitude.values[2].den

                    lat = lat_degrees + lat_minutes / 60.0 + lat_seconds / 3600.0
                    lng = lng_degrees + lng_minutes / 60.0 + lng_seconds / 3600.0
            
                    lat_ref = str(tags.get('GPS GPSLatitudeRef')).upper()
                    lng_ref = str(tags.get('GPS GPSLongitudeRef')).upper()
            
                    if lat_ref == 'S':
                        lat = -lat
                    if lng_ref == 'W':
                        lng = -lng
                    if altitude:
                        altitude = altitude.values[0].num / altitude.values[0].den
                    else:
                        altitude = None    

                    return lat, lng, altitude, image_path


            else:
                return None, None ,None, None
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None, None, None, None

def process_folder(folder_path, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['File Name', 'File Path', 'Latitude', 'Longitude', 'Altitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith('.JPG') or filename.endswith('.JPEG'):
                    image_path = os.path.join(root, filename)
                    lat, lng, alt, img_path = extract_gps(image_path)
                    if lat is not None and lng is not None:
                        writer.writerow(
                            {
                            'File Name': filename,
                            'File Path': img_path,
                            'Latitude': lat,
                            'Longitude': lng,
                            'Altitude': alt }
                        
                        )

# Example usage
folder_path = r"E:\Ortho_mapping_tutorial_Drone_data\Ortho mapping tutorial_Drone data\images"
output_file = r'E:\Ortho_mapping_tutorial_Drone_data\Ortho mapping tutorial_Drone data\output.csv'
process_folder(folder_path, output_file)