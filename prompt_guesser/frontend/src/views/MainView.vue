<template>
  <div class="main-view">
    <v-card
      class="mx-auto my-12"
      max-width="800"
      elevation="5"
    >
      <!--template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template-->

      <v-card-title class="d-align-center game-title">Prompt Guesser</v-card-title>

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
                @click="showDialog"
              >
                Join Game
              </v-btn>
            </v-col>
          </v-row>
        </v-container>

        <v-container v-if="dialogVisibility">
          <v-divider class="mx-4"></v-divider>
          <v-row>
            <!-- Room Join Input -->
              <v-text-field
                label="Room Name"
                v-model="roomTextInput"
                style="text-transform: uppercase;"
                maxlength="5"
                @input="roomTextInput = roomTextInput.toUpperCase()"
              ></v-text-field>

            <!-- Room Join Button -->
            <v-col>
               <v-btn
                color="deep-purple lighten-2"
                text
                @click="join"
               >
                Join
               </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>

    <!-- Join Dialog -->
    <!--div v-if="dialogVisibility">
      <v-dialog>
        <v-card title="Dialog">
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
              text="Close Dialog"
              @click="showDialog"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div-->
  </div>
</template>

<!-- Setup -->
<script setup lang="ts">
// Vue Imports
import { computed, ref, onMounted, onUnmounted, provide } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import IntroSubview from './subviews/IntroSubview.vue';

// Styles
import '../styles/MainView.scss';

// Router
const router = useRouter();

// References
const dialogVisibility = ref(false);  // Whether or not to show the dialog
const roomTextInput = ref(""); // Text input for the room

const showDialog = () => {
  dialogVisibility.value = true;
}

// Create a new room
const create = () => {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ player_name: '1' })
  };

  fetch('http://127.0.0.1:8000/api/sessions', requestOptions)
    .then(response => response.json())
    .then((data) => {
      var t = '/room/' + data.session_name;
      //console.log(t);
      router.push({
        path: t,
        query: {
          data: JSON.stringify({player: 1})
        }
      });
    });
}

// Join an existing room
const join = () => {
  // Try to join a specific room
  //console.log(roomTextInput.value);

  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ player_name: '2' })
  };

  fetch('http://127.0.0.1:8000/api/sessions/' + roomTextInput.value + '/join', requestOptions)
    .then(response => response)
    .then((data) => {
      //console.log(data);
      var t = '/room/' + roomTextInput.value;
      console.log(data);
      if (data.status == 200){
        router.push({
          path: t,
          query: {
            data: JSON.stringify({player: 2})
          }
        });
      }
    });
}

</script>