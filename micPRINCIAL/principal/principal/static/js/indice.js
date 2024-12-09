let cliente = "";

//FUNCION PARA MOSTRAR EL NOMBRE DEL CLIENT EEN LA PAGINA PRINCIAPL
//SIEMPRE Y CUANDO INICISE SESION
const estadoLOGIN = async () => {
    const response = await fetch('autenticado');
    const estado = await response.json();
    let h1 = document.getElementsByClassName("estado");
    
    if (estado.user !== "no autenticado" && estado.user !== null) {
        h1[0].innerHTML += "Sesion iniciada como: " + estado.user;
        cliente = estado.user;
    } else {
        h1[0].innerHTML += "Sesion no iniciada";   
        cliente = "CLIENTE NO IDENTIFICADO"; 
    }
}

document.addEventListener('DOMContentLoaded', function() {
    postPedido();
});
//FUNCION PARA ENVIAR LOS DATOS AL BACKEND 
const postPedido = async () => {
    await estadoLOGIN();
    let clientePOST = cliente;
    
    // Obtener el token CSRF
    const cookieCSRF = getCookie('csrftoken');
    
    const btnsComprar = document.getElementsByClassName("btnComprar");
    for (let i = 0; i < btnsComprar.length; i++) {
        btnsComprar[i].addEventListener("click", function() {
            Swal.fire({
                title: "COMPRA EXITOSA",
                text: "TU PEDIDO FUE PROCESADO CORRECTAMENTE",
                icon: "success"
            });

            let producto, precio, descripcion;
            if (i == 0) {
                producto = "SAMSUNG GALAXY A51";
                precio = "1200";
                descripcion = "SIN DETALLES";
            }
            if (i == 1) {
                producto = "IPHONE 15 PRO MAX";
                precio = "6000";
                descripcion = "SIN DETALLES";
            }
            if (i == 2) {
                producto = "XIAOMI POCO X3 PRO";
                precio = "2500";
                descripcion = "SIN DETALLES";
            }
            
            let datos = {
                'producto': producto,
                'precio': precio,
                'descripcion': descripcion,
                'cliente': clientePOST
            };
            
            // Enviar la solicitud POST para registrar el pedido
            fetch('registerPedido', {
                method: 'POST',
                headers: {
                    'content-Type': 'application/json',
                    'X-CSRFToken': cookieCSRF
                },
                body: JSON.stringify(datos)
            });
        });
    }
};

//funcion para obtener la cookie de falsificaciones csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verificar si esta cookie tiene el nombre especificado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
