<template>
  <v-container class="text-center">
      <div class="text-h6 font-weight-bold start-text">CHOOSE A STARTING POINT</div>
  </v-container>
  <v-container class="text-center">
    <v-btn
      prepend-icon="mdi-plus"
      stacked
      rounded="circle"
      class="ma-6 btn-reactive"
      @click="new_analysis"
      variant="outlined"
    >
      TEST
    </v-btn>
    <v-btn
      prepend-icon="mdi-folder"
      stacked
      rounded="circle"
      class="ma-6 btn-reactive"
      @click="open_analysis"
      variant="outlined"
    >
      Test
    </v-btn>
  </v-container>
</template>

<!-- Setup -->
<script setup lang="ts">
// Vue Imports
import { computed, ref, onMounted, onUnmounted, inject } from 'vue';

</script>