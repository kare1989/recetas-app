const CACHE_NAME = 'recetas-cache-v2';
const urlsToCache = [
  '/',
  '/static/css/style.css',
  '/static/images/icon-128.png'
];

// Instalación del Service Worker y caché inicial
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache).catch(err => {
          console.error('Error al cachear recursos:', err);
        });
      })
  );
});

// Activación y limpieza de cachés viejas
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
});

// Intercepción de peticiones para servir desde caché
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
