<template>
  <!-- Waiting Area -->
  <div v-if="!isReady" id="waiting">
    <div id="room-id" class="top-bar">
      <div>
        <h2 class="room-text">Room {{ roomName }}</h2>
      </div>
    </div>

    <v-container fill-height fluid>
      <v-row align="center" justify="center">
        <v-progress-circular indeterminate :size="100" :width="10"></v-progress-circular>
      </v-row>

      <v-row align="center" justify="center" class="waiting-text">
        <h3>Waiting for player 2 to join...</h3>
      </v-row>
    </v-container>
  </div>
  
  <!-- Game Area -->
  <v-container v-if="isReady" id="game-area">
    <!-- Top Bar -->
    <div id="scores" class="top-bar">
      <v-row>
        <!-- P1 Score -->
        <v-col align="left">
          <div id="p1-score" class="p1-score">
            <h1>{{ playerOneScore }}</h1>
          </div>
        </v-col>

        <v-col align="center">
          <div id="round" class="round">
            <h2>Round {{ round }}/3</h2>
          </div>
        </v-col>

        <!-- P2 Score -->
        <v-col align="right">
          <div id="p2-score" class="p2-score">
            <h1>{{ playerTwoScore }}</h1>
          </div>
        </v-col>
      </v-row>
    </div>

    <!-- Prompt Chooser -->
    <v-row align="center" v-if="role == 'chooser'">
      <v-col>
        <!-- Image Button List -->
        <v-container align="center">
          <v-row>
            <v-col>
              <img class="styled-image" :src="img1">
            </v-col>

            <v-col>
              <img class="styled-image" :src="img2">
            </v-col>

            <v-col>
              <img class="styled-image" :src="img3">
            </v-col>
          </v-row>
        </v-container>

        <!-- Prompt Text Field -->
        <v-container align="center">
          <v-row>
            <v-textarea
              :bg-color="playerNumber == 1 ? 'light-blue' : 'red-lighten-1'"
              label="Enter a prompt"
              variant="solo-filled"
              v-model="promptValue"
            ></v-textarea>
          </v-row>
        </v-container>

        <!-- Submit Button -->
        <v-container align="center">
          <v-row justify="center">
            <v-btn
              color="lighten-2"
              text
              @click="submitPrompt"
            >
              Submit
            </v-btn>
          </v-row>
        </v-container>
      </v-col>
    </v-row>

    <!-- Prompt Guesser -->
    <div align="center" v-if="role == 'guesser'">
      <!-- Waiting State -->
      <v-container fill-height fluid>
        <v-row align="center" justify="center">
          <v-progress-circular indeterminate :size="100" :width="10"></v-progress-circular>
        </v-row>

        <v-row align="center" justify="center" class="waiting-text">
          <h3>Waiting for Player {{ playerNumber.value == 1 ? '2' : '1' }}</h3>
        </v-row>
      </v-container>


      <!-- Guessing State -->
      
    </div>

    <!-- Reveal Stage -->
    <transition>
      <v-row>

      </v-row>
    </transition>
  </v-container>
</template>

<!-- Setup -->
<script setup lang="ts">
// Vue Imports
import { computed, ref, onMounted, onUnmounted, provide } from 'vue';
import { useRoute, useRouter } from 'vue-router';

// Styles
import '../styles/Room.scss';

// References
const isReady = ref(false); // Whether or not the game is ready to start
const roomName = ref(""); // The current room name
const playerNumber = ref(0); // The current player number
const playerOneScore = ref(0); // The current player 1 score
const playerTwoScore = ref(0); // The current player 2 score
const round = ref(1); // The current round
const role = ref(""); // The current role of the player
const promptValue = ref(""); // Prompt value

// Images
const img1 = ref("");
const img2 = ref("");
const img3 = ref("");

// Router
const router = useRouter();

// Methods
const submitPrompt = () => {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 'prompt': promptValue.value })
  };

  //   console.log(router.currentRoute._rawValue)
  var session_id = roomName.value;
  //console.log(session_id);
  //console.log(typeof(session_id));
  fetch('http://127.0.0.1:8000/api/sessions/' + session_id + '/process-prompt', requestOptions)
    .then(response => response.json())
    .then((data) => {
      img1.value = data.images[0];
      img2.value = data.images[1];
      img3.value = data.images[2];
    });
}


// Polling
var pollState = () => {
  const requestOptions = {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' }
  };

  //   console.log(router.currentRoute._rawValue)
  var session_id = roomName.value;
  //console.log(session_id);
  //console.log(typeof(session_id));
  fetch('http://127.0.0.1:8000/api/sessions/' + session_id, requestOptions)
    .then(response => response.json())
    .then((data) => {
      //console.log(data);
      if (data.player_one_name && data.player_two_name){
        // The game is ready to start
        isReady.value = true
      }
    });
}

onMounted(() => {
  // Get Initial State Data
  var fullPath = router.currentRoute._rawValue.fullPath;
  var arr = fullPath.split("?")[1].split("=");
  roomName.value = fullPath.substring(6, 11);
  var queryData = JSON.parse(decodeURI(arr[1]));
  playerNumber.value = queryData.player;
  if (playerNumber.value == 1){
    role.value = "chooser";
  }
  else {
    role.value = "guesser";
  }
  console.log("Role: " + role.value);
  //console.log(queryData);

  // Poll
  setInterval(pollState, 1000);
});

console.log("YOU ARE NOW IN TEST");

</script>