import requests

def get_token(client_id, client_secret, token_url):
    response = requests.post(token_url, auth=(client_id, client_secret), timeout=30)
    response.raise_for_status()
    token_data = response.json()
    access_token = token_data.get("access_token")
    token_type = token_data.get("token_type")
    print(f"Access Token: {access_token}")
    print(f"Token Type: {token_type}")
    if not access_token:
        print("Error: Failed to retrieve access token.")

#Adding comment for testing
def get_new_token(client_id, client_secret, token_url):
    response = requests.post(token_url, auth=(client_id, client_secret), timeout=30)
    response.raise_for_status()
    token_data = response.json()
    access_token = token_data.get("access_token")
    token_type = token_data.get("token_type")
    print(f"Access Token: {access_token}")
    print(f"Token Type: {token_type}")
    if not access_token:
        print("Error: Failed to retrieve access token.")

if __name__=="__main__":
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    token_url = "https://your_token_url"
    bearer_token = get_token(client_id, client_secret, token_url)
    print(f"Bearer Token: {bearer_token}")
