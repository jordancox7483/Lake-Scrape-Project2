import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope (you may adjust based on your needs)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Path to your credentials JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\jcox\\Documents\\Lake Scrape Project\\lake-level-projact-32ee90824bdd.json', scope)

# Authorize the client
client = gspread.authorize(credentials)

# Name of the Google Sheet where you want to write the data
sheet_name = "LakeTracking"

# Open the specified Google Sheet
sheet = client.open(sheet_name)

# Select the first worksheet
worksheet = sheet.get_worksheet(0)  # Assuming you want to write to the first sheet

# URL of the webpage containing the tables
url = 'https://ww4.cubecarolinas.com/lake/levels?orgID=3'

# Send a request to fetch the HTML content of the page
response = requests.get(url)
response.raise_for_status()  # Ensure we notice bad responses

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the specific table by its id
grid_table = soup.find('table', {'id': 'GridView1'})
form_table = soup.find('table', {'id': 'FormView1'})

# Extract the rows of the grid table
grid_rows = grid_table.find_all('tr')

# Define a function to extract text from a table cell (td)
def get_cell_text(row, cell_index):
    cells = row.find_all('td')
    return cells[cell_index].get_text(strip=True) if len(cells) > cell_index else None

# Extract the timestamp from the form table
timestamp_row = form_table.find_all('tr')[0]  # Assuming the timestamp is in the first row
timestamp = get_cell_text(timestamp_row, 0)  # First Column

# Initialize a list for data
data = []

# Iterate through rows to find and extract the specific field
for row in grid_rows[1:]:  # Skip the header row
    # Extracting cells text from each row (e.g., assuming first cell is lake name and second is level)
    lake_name = get_cell_text(row, 0)
    lake_altitude = get_cell_text(row, 1)
    lake_level = get_cell_text(row, 2)
   
    # Append the data to the list
    data.append([lake_name, lake_level, timestamp])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['lake_name', 'lake_level', 'timestamp'])

# Convert DataFrame to list of lists (values in each row)
values = df.values.tolist()




# Initialize a list for new data
new_data = []

# Iterate through rows to find and extract the specific field (similar to your current approach)
for row in grid_rows[1:]:  # Skip the header row
    lake_name = get_cell_text(row, 0)
    lake_altitude = get_cell_text(row, 1)
    lake_level = get_cell_text(row, 2)
    new_data.append([lake_name, lake_level, timestamp])

# Get existing data from the worksheet
existing_data = worksheet.get_all_values()

# Combine existing data with new data
combined_data = existing_data + new_data

# Append the combined data to the worksheet
worksheet.clear()  # Clear existing data (optional, if you want to overwrite everything)
worksheet.append_rows(combined_data)

print(f'Data successfully appended to {sheet_name}!')
