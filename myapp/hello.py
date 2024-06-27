import fire

def hello(name="World my world"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
