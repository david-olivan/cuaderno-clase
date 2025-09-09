document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        // Agregar la clase que iniciará la animación después de 1,5 segundos
        setTimeout(() => {
            alert.classList.add('fade-out');
        }, 1500);

        // Remover el elemento después de que la animación termine
        setTimeout(() => {
            alert.remove();
        }, 2000); // 1500ms + 500ms de la animación
    });
});
