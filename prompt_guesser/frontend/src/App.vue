<!-- App.vue -->
<template>
  <div>
    <main class="d-flex justify-center align-center">
      <router-view v-slot="{ Component, route }">
        <transition :name="route.meta.transition" mode="out-in">
          <component :is="Component" :key="$route.path + rid" ref="mountedComponent"/>
        </transition>
      </router-view>
    </main>
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