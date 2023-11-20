function verifier() {
  if (document.getElementById("answer").value == "Otis" || document.getElementById("answer").value == "otis"){
     alert("Bravo vous avez trouvé le code pour passer")
     window.location.href = '../data/nothing.html';
  }
  else{
     alert("ça n'a pas l'air de fonctionner")
  }
}

function verifier2() {
  if (document.getElementById("answer").value == "veni vidi vici" || document.getElementById("answer").value == "Veni Vidi Vici"){
     alert("Bravo vous avez trouvé le code pour passer")
     window.location.href = '../data/cesar.html';
  }
  else{
     alert("ça n'a pas l'air de fonctionner")
  }
}