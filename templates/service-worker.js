const CACHE_NAME = 'recetas-cache-v1';
const urlsToCache = [
  '/',
  '/static/css/style.css',
  '/static/images/icon-192.png',
  '/static/images/icon-512.png',
  '/static/images/screenshot-wide.png',
  '/static/images/screenshot-mobile.png',
  '/manifest.json'
];

// Instalar y cachear archivos
self.addEventListener('install', event => {
  console.log('📦 Instalando Service Worker...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('✅ Archivos cacheados');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activar y limpiar caché vieja
self.addEventListener('activate', event => {
  console.log('🚀 Activando Service Worker...');
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
});

// Interceptar peticiones y responder desde caché o red
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
