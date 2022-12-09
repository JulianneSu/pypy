n = int(input())
vse = set([input() for i in range(n)])
dni = int(input())
bluda = set()
for i in range(dni):
    m = int(input())
    odin = [input() for i in range(m)]
    bluda = bluda | set(odin)
if len(vse - bluda) == 0:
    print('Готовить нечего')
else:
    delta = vse - bluda
    print('\n'.join(delta))
  #  for i in len(delta):
