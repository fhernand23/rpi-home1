from imgurpython import ImgurClient
from auth_imgur import imgur_client_id,imgur_client_secret

path= "static/img1.jpg"

client = ImgurClient(imgur_client_id, imgur_client_secret)

# Example request
# items = client.gallery()
# for item in items:
#     print(item.link)

result = client.upload_from_path(path, config=None, anon=True)
print(result)
print(result['link'])
for key, value in result.items():
    print(key, value)
