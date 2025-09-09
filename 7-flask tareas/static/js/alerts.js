document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        // Agregar la clase que iniciará la animación después de 3 segundos
        setTimeout(() => {
            alert.classList.add('fade-out');
        }, 1500);

        // Remover el elemento después de que la animación termine
        setTimeout(() => {
            alert.remove();
        }, 2000); // 3000ms + 500ms de la animación
    });
});
