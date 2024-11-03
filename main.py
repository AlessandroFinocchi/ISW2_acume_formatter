import pandas as pd


# Function to compute the new columns
def extract_classifier(s):
    parts = s.split('_')
    return parts[1] if len(parts) > 2 else ''


def extract_feature_selection(s):
    parts = s.split('_')
    return parts[2] if len(parts) > 3 else ''


def extract_balancing(s):
    parts = s.split('_')
    return parts[3] if len(parts) > 4 else ''


def extract_cost_sensitiveness(s):
    parts = s.split('_')
    return parts[4] if len(parts) > 5 else ''


project_path = '..//..//ACUME//ACUME//'
# Read the CSV file into a DataFrame
project_list = {'acume_avro', 'acume_bookkeeper'}
for project in project_list:
    df = pd.read_csv(project_path + project + '.csv')

    # Compute the lengths new columns
    df['Classifier'] = df['Filename'].apply(extract_classifier)
    df['Feature_Selection'] = df['Filename'].apply(extract_feature_selection)
    df['Balancing'] = df['Filename'].apply(extract_balancing)
    df['Cost_Sensitive'] = df['Filename'].apply(extract_cost_sensitiveness)

    # Insert the new columns
    cols = df.columns.tolist()
    insert_pos = cols.index('Filename') + 1  # position to insert after 'A'
    cols.insert(insert_pos, 'Classifier')
    cols.insert(insert_pos + 1, 'Feature_Selection')
    cols.insert(insert_pos + 2, 'Balancing')
    cols.insert(insert_pos + 3, 'Cost_Sensitive')

    # Reorder the DataFrame columns
    df = df[cols]

    # Save the updated DataFrame back to a CSV file
    df.to_csv(project + '_final.csv', index=False)

    print(df)
