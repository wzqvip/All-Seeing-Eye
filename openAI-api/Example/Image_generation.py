"""
    https://platform.openai.com/docs/guides/images/language-specific-tips
    The image generations endpoint allows you to create an original image given a text prompt. 
    Generated images can have a size of 256x256, 512x512, or 1024x1024 pixels. Smaller sizes are faster to generate. 
    You can request 1-10 images at a time using the n parameter.

"""

response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']


"""
Variations
The image variations endpoint allows you to generate a variation of a given image.
"""
response = openai.Image.create_variation(
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']


