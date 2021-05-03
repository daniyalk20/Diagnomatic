<template>
  <div class="contact">
    <h1>This is a Contact Page</h1>
  </div>
    <HelloWorld/>
</template>
<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Contact',
  components: {
    HelloWorld
  }
}
</script>