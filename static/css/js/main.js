if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/static/sw.js').then(function(reg) {
      console.log('Service worker registrado.', reg);
    }).catch(function(err) {
      console.warn('Falló registro SW:', err);
    });
  });
}

// Manejo del prompt de instalación (opcional)
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  // Aquí podrías mostrar un botón personalizado para 'Instalar'
});

function showInstallPrompt() {
  if (deferredPrompt) {
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choiceResult) => {
      deferredPrompt = null;
    });
  }
}