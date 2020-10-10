import random
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='Interface')


@app.route("/fifo", methods=['POST'])
def fifo():
	qtd_quadros = int(request.form['qtd_quad'])
	seqtype = request.form['seqtype']
	qtd_seq = request.form['qtd_seq']

	if seqtype == "Aleatória":
		seq_referencia = [random.randint(0,9) for i in range(int(qtd_seq))]
	else: 
		qtd_seq.replace(" ", "")	
		seq_referencia = qtd_seq.split(",") 

	quadros = []
	falta_paginas = 0
	pit = 0

	for r in seq_referencia: 
		if r not in quadros:
			falta_paginas += 1

			if len(quadros) == qtd_quadros:
				quadros.pop(0)
			quadros.append(r)
        
		else:
			pit += 1
		print(quadros)
	
	
	return render_template("fifo.html", falta_paginas=falta_paginas, pit=pit, quadros=quadros, seq_referencia =seq_referencia, qtd_quadros=qtd_quadros) #retorna o template fifo.html, passando os parametros falta_paginas, pit, quadros, e seq_referencia
	

@app.route("/")
def main():
	return render_template('index.html')


if __name__ == "__main__":
	app.run()


