function carregar() {

    var msg = window.document.getElementById('msg')
    // var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minuto = data.getMinutes()
    // var hora = 10
    // msg.innerHTML = `Agora são ${hora}:${minuto} horas.`

    if (hora >= 0 && hora <= 12) {
        // msg.innerHTML = `Bom dia, agora são ${hora} horas e ${minuto} minutos.`
        msg.innerHTML = `Bom dia!`

    } else if (hora > 12 && hora < 18) {
        // msg.innerHTML = `Boa tarde, agora são ${hora} horas e ${minuto} minutos.`
        msg.innerHTML = `Boa tarde!`
    } else {
        // msg.innerHTML = `Boa noite, agora são ${hora} horas e ${minuto} minutos.`
        msg.innerHTML = `Boa noite!`
    }

}