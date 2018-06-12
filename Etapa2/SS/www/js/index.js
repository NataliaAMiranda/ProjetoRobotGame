var cacas     = [];
var flagpausa = 0;

function pagInd() {
	alert("Página temporariamente indisponível!");
}

function envia(dir) {
	console.log('Inicializando função...');
	var pass = document.getElementById('passos').value;
	console.log('passos');
	console.log(pass);
  var enviaJSON = dir;
  var enviaJSON1 = pass;
  alert(enviaJSON);
  alert(enviaJSON1);
  var info = new Object();
  info['dir'] = dir;
  info['steps'] = pass;
  var info_JSON = JSON.stringify(info);
  $.ajax({
    type       : "PUT",
    url        : "http://localhost:5040/atualiza",
    crossDomain: true,
    data       : info_JSON,
    async      : false,
    dataType   : 'json',
    contentType: 'application/json; charset=utf-8',
    complete: function() {
    		console.log('complete...');
        $('#loading_image').hide();
    },
    success    : function(response) {
    	console.log('success...');
      if(response['ok'] != (-1)) {
        alert('ok');
        console.log('if...');

        retornaFlagPausa();
      }
      else {
        alert('Erro.');
      }
    },
    error      : function() {
      alert('Falha na comunicação com o servidor! \n Verifique sua conexão.');
    }
  });
  console.log('terminando função...');
}

function iniciaFilaSA() {
	$.ajax({
		url: 'http://localhost:5030/ler_cadastro',
		type: 'GET'
  });
  
  $.ajax({
		url: 'http://localhost:5030/ler_pausa',
		type: 'GET'
  });
}

function play() {
	$.ajax({
    url: 'http://localhost:5030/flags',
    type: 'GET',
    dataType: "json",
  	contentType: 'application/json; charset=utf-8',
  	url: "http://localhost:5030/flags",
  	success: function(data){
  		x = (data['flags'][0]['inicio']); 
  		if(x === 0) {
  			console.log('valor de x:' + x);
  			alert('Aguarde o juiz iniciar a partida!');
  			
  			return;
  		}
  		/* Gera as caças:
  		 * curl -i http://localhost:5000/robos/inicio/0 */
  		if (data['flags'][0]['modo'] === 0){
				alert('O jogo irá operar em modo manual!');
				retornaFlagPausa();
		  	window.location.href="./play.html";
		  	
		  	return;
			}
			
			alert('O jogo irá operar em modo automático!');
			return 1;							
		},
    error: function () {
    	alert('Falha na comunicação com o servidor! \n Verifique sua conexão.');
    }
  });
}

function retornaFlagPausa() {
  $.ajax({
		url: 'http://localhost:5030/flagpausa',
    type: 'GET',
    success: function (response) {
      console.log(response);
      if (!response) {
        alert('Não foi encontrado nenhuma resposta');

        return;
      }

      this.flagpausa = response.pausa;

      if (this.flagpausa === 1) {
        alert('Não é possível executar a jogada pois o jogo está pausado pelo Juiz!');

        return;
      }

      retornaFlags();
    }
  });
}

function retornaFlags() {
  $.ajax({
    url: 'http://localhost:5030/flags',
    type: 'GET',
    success: function (response) {
      if (!response) {
        alert('Não foi possível obter as Caças');

        return;
      }

      this.cacas = response.flags[0]['cacas'];

      if (!this.cacas) {
        alert('Não existe nenhuma caça ativa no momento.');
        document.getElementById('passos').disabled = true; 
  			document.getElementById('button1').disabled = true; 
  			document.getElementById('button2').disabled = true; 
  			document.getElementById('button3').disabled = true; 
  			document.getElementById('button4').disabled = true; 
        return;
      }
     	if(this.cacas.length > 0) {
     		document.getElementById('passos').disabled = false; 
  			document.getElementById('button1').disabled = false; 
  			document.getElementById('button2').disabled = false; 
  			document.getElementById('button3').disabled = false; 
  			document.getElementById('button4').disabled = false; 
     		var i;
     		for(i = 0; i < this.cacas.length-3; i++) {
     			document.getElementById('caca'+i).innerHTML = "(" + this.cacas[i][0] + "," + this.cacas[i][1] + ")";
     		}
     	}
    },
    error: function () {
    	alert('Não foi possível acessar o servidor');
    }
  });
}
