<template>
  <v-progress-circular v-if="!isReady" indeterminate :size="43" :width="7"></v-progress-circular>
</template>

<!-- Setup -->
<script setup lang="ts">
// Vue Imports
import { computed, ref, onMounted, onUnmounted, provide } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const isReady = ref(false)




// Router
const router = useRouter();

 var f = () => {
    const requestOptions = {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
    // body: JSON.stringify({ player_name: 'TEST' })
  };
//   console.log(router.currentRoute._rawValue)
  var session_id = router.currentRoute._rawValue.fullPath.substring(6);
  fetch('http://127.0.0.1:8000/api/sessions/' + session_id, requestOptions)
    .then(response => response.json())
    .then((data) => {
      console.log(data);
      if (data.player_one_name.length > 0) {
        isReady.value = true
      }
    });
 }

 onMounted(() => {
    setInterval(f, 1000)
    // console.log("Working")
 })

console.log("YOU ARE NOW IN TEST");

</script>