// Vue imports
import { createApp } from 'vue';
import { createMemoryHistory, createRouter } from 'vue-router';

// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
const vuetify = createVuetify({
  components,
  directives,
});

// Base style
import './styles/index.scss';

// Main app
import App from './App.vue';

// Views
import Main from './views/MainView.vue';
import Room from './views/Room.vue';
import Final from './views/FinalView.vue';

// Router
const router = createRouter({
history: createMemoryHistory(), // Memory-based routing
  routes: [
    {
      path: '/',
      component: Main,
      props: true,
      meta: {
        transition: 'fade'
      }
    },
    {
      path: '/room/:id',
      component: Room,
      meta: {
        transition: 'fade'
      }
    },
    {
      path: '/finish/:id',
      component: Final,
      meta: {
        transition: 'fade'
      }
    }
  ]
});

// Create the Vue application
createApp(App).use(router).use(vuetify).mount('#main');