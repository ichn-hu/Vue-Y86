<template>
  <div id="showResult">
    <div id="resultBackground">
    </div>

    <v-dialog v-model="dialog" fullscreen transition="dialog-bottom-transition" :overlay=false scrollable>
      <v-btn icon @click.native="dialog = false">
        <v-icon>close</v-icon>
      </v-btn>
    </v-dialog>

    <v-navigation-drawer v-model="primaryDrawer.model" :permanent="primaryDrawer.type === 'permanent'" :temporary="primaryDrawer.type === 'temporary'"
                         :clipped="primaryDrawer.clipped" :floating="primaryDrawer.floating" :mini-variant="primaryDrawer.mini" fixed
                         overflow app style="background: rgba(255, 255, 255, 0.35);box-shadow: 0 1px 5px rgba(0, 0, 0, 0.25);">

      <v-container grid-list-md text-xs-center>
        <v-layout row>
          <v-flex xs4 class="my-1">
            <v-card tile>
              <m-card title="ZF" :value="cur.cc.ZF">
              </m-card>
            </v-card>
          </v-flex>
          <v-flex xs4 class="my-1">
            <v-card tile>
              <m-card title="SF" :value="cur.cc.SF">
              </m-card>
            </v-card>
          </v-flex>
          <v-flex xs4 class="my-1">
            <v-card tile>
              <m-card title="OF" :value="cur.cc.OF">
              </m-card>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
      <v-container grid-list-md text-xs-center>
        <v-layout row wrap>
          <v-flex d-flex xs6>
            <m-card title="EAX" :value="cur.reg.EAX"></m-card>
          </v-flex>
          <v-flex d-flex xs6>
            <m-card title="ECX" :value="cur.reg.ECX"></m-card>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex d-flex xs6>
            <m-card title="EDX" :value="cur.reg.EDX"></m-card>
          </v-flex>
          <v-flex d-flex xs6>
            <m-card title="EBX" :value="cur.reg.EBX"></m-card>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex d-flex xs6>
            <m-card title="ESP" :value="cur.reg.ESP"></m-card>
          </v-flex>
          <v-flex d-flex xs6>
            <m-card title="EBP" :value="cur.reg.EBP"></m-card>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex d-flex xs6>
            <m-card title="ESI" :value="cur.reg.ESI"></m-card>
          </v-flex>
          <v-flex d-flex xs6>
            <m-card title="EDI" :value="cur.reg.EDI"></m-card>
          </v-flex>
        </v-layout>
      </v-container>
      <v-container>
        <v-layout row wrap>
          <v-flex d-flex xs12>
            <v-layout row wrap>
              <v-flex d-flex>
                <v-layout row wrap>
                  <v-flex d-flex v-for="(val, name) in cur.mem" :name="name" :val="val" :key="name" xs12 class="my-1">
                    <m-card :title="name" :value="val">
                    </m-card>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-container>
    </v-navigation-drawer>

    <v-toolbar app absolute :clipped-left="primaryDrawer.clipped">
      <v-toolbar-side-icon @click.stop="primaryDrawer.model = !primaryDrawer.model" v-if="primaryDrawer.type !== 'permanent'"></v-toolbar-side-icon>
      <v-toolbar-title style="font-family: 'modeno'">The Modern Y86 Simulator</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn @click.stop="dialog = true" :fab="true" :small="true" class="elevation-0">
        <v-icon medium>fa-line-chart</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <v-container grid-list-xl text-xs-center>
        <v-layout align-center justify-center style="background: rgba(255, 255, 255, 0.35);box-shadow: 0 1px 5px rgba(0, 0, 0, 0.25);">
          <v-flex xs12>
            <m-writeback v-bind="cur.W"></m-writeback>
            <m-memory v-bind="cur.M"></m-memory>
            <m-execute v-bind="cur.E"></m-execute>
            <m-decode v-bind="cur.D"></m-decode>
            <m-fetch v-bind="cur.F"></m-fetch>
            <v-card-actions>
              <v-btn :ripple="false"  :cyc="cyc" @click.stop="changeFreq = true">
                <v-icon medium left>
                  fa-clock-o
                </v-icon>
                {{ cyc }}
              </v-btn>

              <v-dialog v-model="changeFreq" max-width="500px">
                <v-card>
                  <v-card-title>
                    Change Frequency
                  </v-card-title>
                  <v-card-text>
                    <v-text-field
                      name="Running Frequency"
                      label="Running Frequency"
                      :value="freq"
                      v-model="freq"
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-dialog>

              <v-btn :ripple="false" :disable="true" style="width: 100%; padding: 0px;">
                <v-slider v-model="cyc" thumb-label step="1" :max="maxCyc" ticks style=" padding: 3px;"></v-slider>
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn @click.stop="renderInit">
                <v-icon>
                  refresh
                </v-icon>
              </v-btn>
              <v-btn @click.stop="renderPrevious">
                <v-icon>fa-backward</v-icon>
              </v-btn>
              <v-btn @click.stop="changeStatus">
                <v-icon v-if="stopped">
                  fa-play
                </v-icon>
                <v-icon v-if="!stopped">
                  fa-pause
                </v-icon>
              </v-btn>
              <v-btn @click.stop="renderNext">
                <v-icon>fa-forward</v-icon>
              </v-btn>
            </v-card-actions>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </div>
</template>
<script>
  import Card from '@/components/misc/card'
  import Fetch from '@/components/stages/Fetch'
  import Decode from '@/components/stages/Decode'
  import Execute from '@/components/stages/Execute'
  import Memory from '@/components/stages/Memory'
  import Writeback from '@/components/stages/Writeback'
  export default {
    components: {
      'm-card': Card,
      'm-fetch': Fetch,
      'm-decode': Decode,
      'm-execute': Execute,
      'm-memory': Memory,
      'm-writeback': Writeback
    },
    data () {
      return {
        result: null,
        maxCyc: 0,
        cyc: -1,
        cur: null,
        dialog: false,
        changeFreq: false,
        stopped: true,
        freq: 10,
        dark: true,
        drawers: ['Permanent', 'Persistent', 'Temporary'],
        primaryDrawer: {
          model: true,
          type: 'persistent',
          clipped: false,
          floating: false,
          mini: false
        },
        footer: {
          fixed: false
        }
      }
    },
    methods: {
      getRegName: function (id) {
        if (id > 7) {
          return '---'
        }
        var ret = {
          0: 'EAX',
          1: 'ECX',
          2: 'EDX',
          3: 'EBX',
          4: 'ESP',
          5: 'EBP',
          6: 'ESI',
          7: 'EDI'
        }[id]
        if (ret) return ret
        return '---'
      },
      switchEndian: function (val) {
        if (val === '---') {
          return '----------'
        }
        if (val.slice(0, 2) === '--' || val.slice(0, 2) === '0x') {
          return val
        }
        return '0x' + val.slice(6, 8) + val.slice(4, 6) + val.slice(2, 4) + val.slice(0, 2)
      },
      renderReg: function () {
      },
      renderIns: function (ins) {
        if (typeof (ins) === 'string') {
          var addr = ins.slice(0, 8)
          var code = ins.slice(9, ins.length)
          if (!addr || !code) {
            return {addr: '--------', code: 'No Instruction'}
          }
          return {addr: addr, code: code}
        } else {
          return ins
        }
      },
      renderThis: function () {
        this.cur = this.result[this.cyc]

        // this.cur.F.name = 'F'
        // this.cur.D.name = 'D'
        // this.cur.E.name = 'E'
        // this.cur.M.name = 'M'
        // this.cur.W.name = 'W'
        // if (this.cur.F.stall || this.cur.F.bubble)
        //     alert('233')
        //     if (this.cur.D.stall || this.cur.D.bubble)
        //     alert('233')
        //     if (this.cur.E.stall || this.cur.E.bubble)
        //     alert('233')
        //     if (this.cur.M.stall || this.cur.M.bubble)
        //     alert('233')
        //     if (this.cur.W.stall || this.cur.W.bubble)
        //     alert('233')

        this.cur.F.ins = this.renderIns(this.cur.F.ins)
        this.cur.D.ins = this.renderIns(this.cur.D.ins)
        this.cur.W.ins = this.renderIns(this.cur.W.ins)
        this.cur.E.ins = this.renderIns(this.cur.E.ins)
        this.cur.M.ins = this.renderIns(this.cur.M.ins)
        this.cur.F.predPC = this.switchEndian(this.cur.F.predPC)
        this.cur.D.valC = this.switchEndian(this.cur.D.valC)
        this.cur.D.valP = this.switchEndian(this.cur.D.valP)
        this.cur.E.valC = this.switchEndian(this.cur.E.valC)
        this.cur.E.valA = this.switchEndian(this.cur.E.valA)
        this.cur.E.valB = this.switchEndian(this.cur.E.valB)
        this.cur.M.valE = this.switchEndian(this.cur.M.valE)
        this.cur.M.valA = this.switchEndian(this.cur.M.valA)
        this.cur.W.valE = this.switchEndian(this.cur.W.valE)
        this.cur.W.valM = this.switchEndian(this.cur.W.valM)
        this.cur.D.rA = this.getRegName(this.cur.D.rA)
        this.cur.D.rB = this.getRegName(this.cur.D.rB)
        this.cur.E.dstE = this.getRegName(this.cur.E.dstE)
        this.cur.E.dstM = this.getRegName(this.cur.E.dstM)
        this.cur.E.srcA = this.getRegName(this.cur.E.srcA)
        this.cur.E.srcB = this.getRegName(this.cur.E.srcB)
        this.cur.M.dstE = this.getRegName(this.cur.M.dstE)
        this.cur.M.dstM = this.getRegName(this.cur.M.dstM)
        this.cur.W.dstE = this.getRegName(this.cur.W.dstE)
        this.cur.W.dstM = this.getRegName(this.cur.W.dstM)
      },
      renderNext: function () {
        if (this.cyc + 1 <= this.maxCyc) {
          ++this.cyc
          return true
        }
        return false
      },
      renderPrevious: function () {
        if (this.cyc - 1 >= 0) {
          --this.cyc
          return true
        }
        return false
      },
      renderInit: function () {
        console.log('render init')
        var maxCyc = 0
        while (this.result[maxCyc]) {
          ++maxCyc
        }
        this.maxCyc = maxCyc - 1
        this.cyc = -1
        this.stopped = true
        console.log(this.maxCyc)
        this.renderNext()
      },
      runThis: function () {
        if (this.stopped) {
          return
        }
        this.stopped = !this.renderNext()
        if (!this.stopped) {
          setTimeout(this.runThis, 1000 / this.freq)
        }
      },
      changeStatus: function () {
        this.stopped = !this.stopped
        if (!this.stopped) {
          this.runThis()
        }
      }
    },
    watch: {
      cyc: function () {
        this.renderThis()
      }
    },
    beforeCreate () {
    },
    beforeMount () {
      this.result = window.result
      this.renderInit()
      this.renderThis()
      this.primaryDrawer.model = false
    }
  }
</script>
<style scoped>
  #showResult {
    position: fixed;
    width: 100%;
    height: 100%;
    background-size: cover;
  }
  #resultBackground {
    display: block;
    height: 99%;
    width: 99%;
    z-index: -1;
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -100;
    /* background: url('/static/bkgd.gif') no-repeat; */
    background: url('/static/bkgd2.gif') no-repeat;
    background-position: center;
    background-size: cover;
    -webkit-filter: blur(5px);
    -moz-filter: blur(5px);
    -o-filter: blur(5px);
    -ms-filter: blur(5px);
    filter: blur(5px);
  }
  #dataPanel {
    background: rgba(255, 255, 255, 0.25);
    border-radius: 5px;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 0.15);
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
    top: 20%;
    left: 10%;
    right: 10%;
    position: fixed;
    z-index: 2;
  }
  .m-row:hover {
    border-radius: 3px;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 2);
  }


</style>
