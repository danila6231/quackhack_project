<template>
  <div class="main-view">
    <v-card
      class="mx-auto my-12"
      max-width="800"
      elevation="5"
    >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>

      <v-card-title class="d-align-center">Prompt Guesser</v-card-title>

      <v-divider class="mx-4"></v-divider>

      <v-card-text>
        <v-container
          class="lighten-5"
        >
          <v-row>
            <!-- New -->
            <v-col>
              <v-btn
                color="deep-purple lighten-2"
                text
                @click="create"
              >
                New Game
              </v-btn>
            </v-col>

            <!-- Join -->
            <v-col>
              <v-btn
                color="deep-purple lighten-2"
                text
                @click="create"
              >
                Join Game
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </div>
</template>

<!-- Setup -->
<script setup lang="ts">
// Vue Imports
import { computed, ref, onMounted, onUnmounted, provide } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import IntroSubview from './subviews/IntroSubview.vue';

// Router
const router = useRouter();

const create = () => {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ player_name: 'TEST' })
  };

  fetch('http://127.0.0.1:8000/api/sessions', requestOptions)
    .then(response => response.json())
    .then((data) => {
      var t = '/room/' + data.session_name;
      //console.log(t);
      router.push(t);
    });
}

</script>