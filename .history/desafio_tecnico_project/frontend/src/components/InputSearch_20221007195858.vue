<script setup>
export default {
  data: function() {
    return{
      state: ''
    }
  }
}
</script>

<template>
  <div>
    <input type="text" class v-model="state"/>
  </div>
</template>

