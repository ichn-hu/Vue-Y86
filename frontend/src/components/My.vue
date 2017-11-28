<template>
  <div>
    <section>
      <h1 class="head" :src="name">Hello! {{ name }}</h1>
    </section>
    <section>
      <button @click="changeName">Change my name</button>
      <button @click="reverseName">Reverse my name</button>
    </section>
  </div>
</template>
<script>
export default {
  name: "my-comp",
  data() {
    return {
      name: "Hu Zhifeng"
    };
  },
  methods: {
    changeName() {
      this.name = "Y86 Pipelined Simulator";
    },
    reverseName() {
      this.name = this.name.split("").reverse().join("");
    }
  }
};
</script>

<style scope>
.head {
  border: 1px solid #1f3fff;
  text-align: center;
}
button {
  color: firebrick;
  background: black;
}
</style>


