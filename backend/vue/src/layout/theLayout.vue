<template>
  <div>
    <theHeader />
    <div style="display:flex">
      <router-view  style="flex: 1"/>
    </div>
  </div>
</template>

<style>
</style>

<script>
import theHeader from "@/components/theHeader";

export default {
  name:"theLayout",
  components :{
    theHeader
  }
}
</script>