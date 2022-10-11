<script setup>

</script>

<template>
  <div>
    <input type="text" v-model="state" @input="filterStates"/>
    <ul class="suggestions">
      <li class="s"></li>

    </ul>
  </div>
</template>

