import subprocess

class ResponsePresenter:
  def __init__(self):
    pass

  def present(self, response):
    subprocess.run(['notify-send', 'Resposta', response, '-t', '10000'])
