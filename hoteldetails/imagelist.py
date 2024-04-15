def imgfinder(images_list): 
  try: 
    return images_list[0] 
  except IndexError: 
    return "some_url"