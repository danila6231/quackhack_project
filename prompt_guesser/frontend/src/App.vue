<!-- App.vue -->
 <template>
  <div>
    <h1>
      HELLO WORLD
    </h1>
  </div>
 </template>

 <!-- Setup -->
<script setup lang="ts">
// Vue Imports
import { ref, onMounted, onUnmounted, provide } from 'vue';
import { useRoute, useRouter } from 'vue-router';

// Styles
import './styles/App.scss';

// Router
const router = useRouter();


</script>