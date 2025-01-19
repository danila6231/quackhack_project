<template>
  <div class="final-view">
    <div id="scores" class="top-bar">
      <v-row>
        <!-- P1 Score -->
        <v-col align="left" style="color: #42a5f5">
          <div id="p1-score" class="p1-score">
            <h1>1</h1>
          </div>
        </v-col>

        <!-- P2 Score -->
        <v-col align="right">
          <div id="p2-score" style="color: #ef5350">
            <h1>1</h1>
          </div>
        </v-col>
      </v-row>
      <div align="center">
        <h1 style="margin-top: 30%">Player 1 winzzz</h1>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import '../styles/Room.scss';
import '../styles/FinalView.scss';
</script>