webpackJsonp([1,3,4,5,6,7],{"4aqQ":function(t,a){},"9NJk":function(t,a){},BRpJ:function(t,a){},JgHD:function(t,a){},"N/0d":function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("xCaS"),r=s("yvKl"),i=s("oGIN"),l=s("RYtK"),n=s("sI6j"),c=s("S8e+"),o={components:{"m-card":e.default,"m-fetch":r.default,"m-decode":i.default,"m-execute":l.default,"m-memory":n.default,"m-writeback":c.default},data:function(){return{result:null,maxCyc:0,cyc:-1,cur:null,dialog:!1,changeFreq:!1,stopped:!0,freq:10,dark:!0,drawers:["Permanent","Persistent","Temporary"],primaryDrawer:{model:!0,type:"persistent",clipped:!1,floating:!1,mini:!1},footer:{fixed:!1}}},methods:{getRegName:function(t){if(t>7)return"---";var a={0:"EAX",1:"ECX",2:"EDX",3:"EBX",4:"ESP",5:"EBP",6:"ESI",7:"EDI"}[t];return a||"---"},switchEndian:function(t){return"---"===t?"----------":"--"===t.slice(0,2)||"0x"===t.slice(0,2)?t:"0x"+t.slice(6,8)+t.slice(4,6)+t.slice(2,4)+t.slice(0,2)},renderReg:function(){},renderIns:function(t){if("string"==typeof t){var a=t.slice(0,8),s=t.slice(9,t.length);return a&&s?{addr:a,code:s}:{addr:"--------",code:"No Instruction"}}return t},renderThis:function(){this.cur=this.result[this.cyc],this.cur.F.ins=this.renderIns(this.cur.F.ins),this.cur.D.ins=this.renderIns(this.cur.D.ins),this.cur.W.ins=this.renderIns(this.cur.W.ins),this.cur.E.ins=this.renderIns(this.cur.E.ins),this.cur.M.ins=this.renderIns(this.cur.M.ins),this.cur.F.predPC=this.switchEndian(this.cur.F.predPC),this.cur.D.valC=this.switchEndian(this.cur.D.valC),this.cur.D.valP=this.switchEndian(this.cur.D.valP),this.cur.E.valC=this.switchEndian(this.cur.E.valC),this.cur.E.valA=this.switchEndian(this.cur.E.valA),this.cur.E.valB=this.switchEndian(this.cur.E.valB),this.cur.M.valE=this.switchEndian(this.cur.M.valE),this.cur.M.valA=this.switchEndian(this.cur.M.valA),this.cur.W.valE=this.switchEndian(this.cur.W.valE),this.cur.W.valM=this.switchEndian(this.cur.W.valM),this.cur.D.rA=this.getRegName(this.cur.D.rA),this.cur.D.rB=this.getRegName(this.cur.D.rB),this.cur.E.dstE=this.getRegName(this.cur.E.dstE),this.cur.E.dstM=this.getRegName(this.cur.E.dstM),this.cur.E.srcA=this.getRegName(this.cur.E.srcA),this.cur.E.srcB=this.getRegName(this.cur.E.srcB),this.cur.M.dstE=this.getRegName(this.cur.M.dstE),this.cur.M.dstM=this.getRegName(this.cur.M.dstM),this.cur.W.dstE=this.getRegName(this.cur.W.dstE),this.cur.W.dstM=this.getRegName(this.cur.W.dstM)},renderNext:function(){return this.cyc+1<=this.maxCyc&&(++this.cyc,!0)},renderPrevious:function(){return this.cyc-1>=0&&(--this.cyc,!0)},renderInit:function(){console.log("render init");for(var t=0;this.result[t];)++t;this.maxCyc=t-1,this.cyc=-1,this.stopped=!0,console.log(this.maxCyc),this.renderNext()},runThis:function(){this.stopped||(this.stopped=!this.renderNext(),this.stopped||setTimeout(this.runThis,1e3/this.freq))},changeStatus:function(){this.stopped=!this.stopped,this.stopped||this.runThis()}},watch:{cyc:function(){this.renderThis()}},beforeCreate:function(){},beforeMount:function(){this.result=window.result,this.renderInit(),this.renderThis(),this.primaryDrawer.model=!1}},v={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{attrs:{id:"showResult"}},[s("div",{attrs:{id:"resultBackground"}}),t._v(" "),s("v-dialog",{attrs:{fullscreen:"",transition:"dialog-bottom-transition",overlay:!1,scrollable:""},model:{value:t.dialog,callback:function(a){t.dialog=a},expression:"dialog"}},[s("v-btn",{attrs:{icon:""},nativeOn:{click:function(a){t.dialog=!1}}},[s("v-icon",[t._v("close")])],1)],1),t._v(" "),s("v-navigation-drawer",{staticStyle:{background:"rgba(255, 255, 255, 0.35)","box-shadow":"0 1px 5px rgba(0, 0, 0, 0.25)"},attrs:{permanent:"permanent"===t.primaryDrawer.type,temporary:"temporary"===t.primaryDrawer.type,clipped:t.primaryDrawer.clipped,floating:t.primaryDrawer.floating,"mini-variant":t.primaryDrawer.mini,fixed:"",overflow:"",app:""},model:{value:t.primaryDrawer.model,callback:function(a){t.$set(t.primaryDrawer,"model",a)},expression:"primaryDrawer.model"}},[s("v-container",{attrs:{"grid-list-md":"","text-xs-center":""}},[s("v-layout",{attrs:{row:""}},[s("v-flex",{staticClass:"my-1",attrs:{xs4:""}},[s("v-card",{attrs:{tile:""}},[s("m-card",{attrs:{title:"ZF",value:t.cur.cc.ZF}})],1)],1),t._v(" "),s("v-flex",{staticClass:"my-1",attrs:{xs4:""}},[s("v-card",{attrs:{tile:""}},[s("m-card",{attrs:{title:"SF",value:t.cur.cc.SF}})],1)],1),t._v(" "),s("v-flex",{staticClass:"my-1",attrs:{xs4:""}},[s("v-card",{attrs:{tile:""}},[s("m-card",{attrs:{title:"OF",value:t.cur.cc.OF}})],1)],1)],1)],1),t._v(" "),s("v-container",{attrs:{"grid-list-md":"","text-xs-center":""}},[s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"EAX",value:t.cur.reg.EAX}})],1),t._v(" "),s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"ECX",value:t.cur.reg.ECX}})],1)],1),t._v(" "),s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"EDX",value:t.cur.reg.EDX}})],1),t._v(" "),s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"EBX",value:t.cur.reg.EBX}})],1)],1),t._v(" "),s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"ESP",value:t.cur.reg.ESP}})],1),t._v(" "),s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"EBP",value:t.cur.reg.EBP}})],1)],1),t._v(" "),s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"ESI",value:t.cur.reg.ESI}})],1),t._v(" "),s("v-flex",{attrs:{"d-flex":"",xs6:""}},[s("m-card",{attrs:{title:"EDI",value:t.cur.reg.EDI}})],1)],1)],1),t._v(" "),s("v-container",[s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{"d-flex":"",xs12:""}},[s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{"d-flex":""}},[s("v-layout",{attrs:{row:"",wrap:""}},t._l(t.cur.mem,function(t,a){return s("v-flex",{key:a,staticClass:"my-1",attrs:{"d-flex":"",name:a,val:t,xs12:""}},[s("m-card",{attrs:{title:a,value:t}})],1)}))],1)],1)],1)],1)],1)],1),t._v(" "),s("v-toolbar",{attrs:{app:"",absolute:"","clipped-left":t.primaryDrawer.clipped}},["permanent"!==t.primaryDrawer.type?s("v-toolbar-side-icon",{on:{click:function(a){a.stopPropagation(),t.primaryDrawer.model=!t.primaryDrawer.model}}}):t._e(),t._v(" "),s("v-toolbar-title",{staticStyle:{"font-family":"'modeno'"}},[t._v("The Modern Y86 Simulator")]),t._v(" "),s("v-spacer"),t._v(" "),s("v-btn",{staticClass:"elevation-0",attrs:{fab:!0,small:!0},on:{click:function(a){a.stopPropagation(),t.dialog=!0}}},[s("v-icon",{attrs:{medium:""}},[t._v("fa-line-chart")])],1)],1),t._v(" "),s("v-content",[s("v-container",{attrs:{"grid-list-xl":"","text-xs-center":""}},[s("v-layout",{staticStyle:{background:"rgba(255, 255, 255, 0.35)","box-shadow":"0 1px 5px rgba(0, 0, 0, 0.25)"},attrs:{"align-center":"","justify-center":""}},[s("v-flex",{attrs:{xs12:""}},[s("m-writeback",t._b({},"m-writeback",t.cur.W,!1)),t._v(" "),s("m-memory",t._b({},"m-memory",t.cur.M,!1)),t._v(" "),s("m-execute",t._b({},"m-execute",t.cur.E,!1)),t._v(" "),s("m-decode",t._b({},"m-decode",t.cur.D,!1)),t._v(" "),s("m-fetch",t._b({},"m-fetch",t.cur.F,!1)),t._v(" "),s("v-card-actions",[s("v-btn",{attrs:{ripple:!1,cyc:t.cyc},on:{click:function(a){a.stopPropagation(),t.changeFreq=!0}}},[s("v-icon",{attrs:{medium:"",left:""}},[t._v("\n                fa-clock-o\n              ")]),t._v("\n              "+t._s(t.cyc)+"\n            ")],1),t._v(" "),s("v-dialog",{attrs:{"max-width":"500px"},model:{value:t.changeFreq,callback:function(a){t.changeFreq=a},expression:"changeFreq"}},[s("v-card",[s("v-card-title",[t._v("\n                  Change Frequency\n                ")]),t._v(" "),s("v-card-text",[s("v-text-field",{attrs:{name:"Running Frequency",label:"Running Frequency",value:t.freq},model:{value:t.freq,callback:function(a){t.freq=a},expression:"freq"}})],1)],1)],1),t._v(" "),s("v-btn",{staticStyle:{width:"100%",padding:"0px"},attrs:{ripple:!1,disable:!0}},[s("v-slider",{staticStyle:{padding:"3px"},attrs:{"thumb-label":"",step:"1",max:t.maxCyc,ticks:""},model:{value:t.cyc,callback:function(a){t.cyc=a},expression:"cyc"}})],1),t._v(" "),s("v-spacer"),t._v(" "),s("v-btn",{on:{click:function(a){a.stopPropagation(),t.renderInit(a)}}},[s("v-icon",[t._v("\n                refresh\n              ")])],1),t._v(" "),s("v-btn",{on:{click:function(a){a.stopPropagation(),t.renderPrevious(a)}}},[s("v-icon",[t._v("fa-backward")])],1),t._v(" "),s("v-btn",{on:{click:function(a){a.stopPropagation(),t.changeStatus(a)}}},[t.stopped?s("v-icon",[t._v("\n                fa-play\n              ")]):t._e(),t._v(" "),t.stopped?t._e():s("v-icon",[t._v("\n                fa-pause\n              ")])],1),t._v(" "),s("v-btn",{on:{click:function(a){a.stopPropagation(),t.renderNext(a)}}},[s("v-icon",[t._v("fa-forward")])],1)],1)],1)],1)],1)],1)],1)},staticRenderFns:[]},u=s("VU/8")(o,v,!1,function(t){s("9NJk")},"data-v-55b0ec1e",null);a.default=u.exports},QA5k:function(t,a){},RYtK:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("EhQ/"),r=s("xCaS"),i={components:{"m-stage":e.default,"m-card":r.default},props:["stat","bubble","stall","ins","operation","valC","valA","valB","dstE","dstM","srcA","srcB"]},l={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("v-tooltip",{attrs:{top:"",disabled:0===t.operation.length}},[s("v-layout",{staticClass:"m-row mx-1  my-1",attrs:{slot:"activator",row:"",wrap:""},slot:"activator"},[s("v-flex",{staticClass:"my-2",attrs:{xs2:"","offset-xs0":""}},[s("m-stage",{attrs:{ins:t.ins,name:"E",stat:t.stat,operation:t.operation,bubble:t.bubble,stall:t.stall}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  px-0 py-0  mx-1 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"valC",value:t.valC}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0 ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valA",value:t.valA}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0 ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valB",value:t.valB}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"dstE",value:t.dstE}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"dstM",value:t.dstM}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"srcA",value:t.srcA}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"srcA",value:t.srcA}})],1)],1),t._v(" "),s("span",[t._l(t.operation,function(a){return s("div",{staticClass:"m-operation"},[t._v("\n                      "+t._s(a)+"\n                  ")])})],2)],1)},staticRenderFns:[]},n=s("VU/8")(i,l,!1,function(t){s("BRpJ")},"data-v-768a9d7e",null);a.default=n.exports},"S8e+":function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("EhQ/"),r=s("xCaS"),i={components:{"m-stage":e.default,"m-card":r.default},name:"Writeback",props:["stat","bubble","stall","ins","operation","Cnd","valE","valM","dstE","dstM"]},l={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("v-tooltip",{attrs:{top:"",disabled:0===t.operation.length}},[s("v-layout",{staticClass:"m-row mx-1 my-1",attrs:{slot:"activator",row:"",wrap:""},slot:"activator"},[s("v-flex",{staticClass:"my-2",attrs:{xs2:"","offset-xs0":""}},[s("m-stage",{attrs:{ins:t.ins,name:"W",stat:t.stat,operation:t.operation,bubble:t.bubble,stall:t.stall}})],1),t._v(" "),s("v-flex",{staticClass:"  my-2  mx-1 px-0 py-0",attrs:{xs1:""}}),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valE",value:t.valE}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valM",value:t.valM}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"dstE",value:t.dstE}})],1),t._v(" "),s("v-flex",{staticClass:" my-2  mx-1 px-0 py-0  ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"dstM",value:t.dstM}})],1)],1),t._v(" "),s("span",[t._l(t.operation,function(a){return s("div",{staticClass:"m-operation"},[t._v("\n        "+t._s(a)+"\n      ")])})],2)],1)},staticRenderFns:[]},n=s("VU/8")(i,l,!1,function(t){s("QA5k")},"data-v-0cd8243c",null);a.default=n.exports},l4N1:function(t,a){},oGIN:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("EhQ/"),r=s("xCaS"),i={components:{"m-stage":e.default,"m-card":r.default},props:["stat","bubble","stall","ins","operation","rA","rB","valC","valP"]},l={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("v-tooltip",{attrs:{top:"",disabled:0===t.operation.length}},[s("v-layout",{staticClass:"m-row mx-1  my-1",attrs:{slot:"activator",row:"",wrap:""},slot:"activator"},[s("v-flex",{staticClass:"my-2",attrs:{xs2:"","offset-xs0":""}},[s("m-stage",{attrs:{ins:t.ins,name:"D",stat:t.stat,operation:t.operation,bubble:t.bubble,stall:t.stall}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0  ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"rA",value:t.rA}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1  px-0 py-0  ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"rB",value:t.rB}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1  px-0 py-0  ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valC",value:t.valC}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1  px-0 py-0  ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valP",value:t.valP}})],1)],1),t._v(" "),s("span",[t._l(t.operation,function(a){return s("div",{staticClass:"m-operation"},[t._v("\n                      "+t._s(a)+"\n                  ")])})],2)],1)},staticRenderFns:[]},n=s("VU/8")(i,l,!1,function(t){s("l4N1")},"data-v-a1d8b498",null);a.default=n.exports},sI6j:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("EhQ/"),r=s("xCaS"),i={components:{"m-stage":e.default,"m-card":r.default},props:["stat","bubble","stall","ins","operation","Cnd","valC","valE","valA","dstE","dstM"]},l={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("v-tooltip",{attrs:{top:"",disabled:0===t.operation.length}},[s("v-layout",{staticClass:"m-row mx-1  my-1",attrs:{slot:"activator",row:"",wrap:""},slot:"activator"},[s("v-flex",{staticClass:"my-2",attrs:{xs2:"","offset-xs0":""}},[s("m-stage",{attrs:{ins:t.ins,name:"M",stat:t.stat,operation:t.operation,bubble:t.bubble,stall:t.stall}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"Cnd",value:t.Cnd}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valE",value:t.valE}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs2:""}},[s("m-card",{attrs:{title:"valA",value:t.valA}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"dstE",value:t.dstE}})],1),t._v(" "),s("v-flex",{staticClass:" my-2   mx-1 px-0 py-0 ",attrs:{xs1:""}},[s("m-card",{attrs:{title:"dstM",value:t.dstM}})],1)],1),t._v(" "),s("span",[t._l(t.operation,function(a){return s("div",{staticClass:"m-operation"},[t._v("\n                      "+t._s(a)+"\n                  ")])})],2)],1)},staticRenderFns:[]},n=s("VU/8")(i,l,!1,function(t){s("4aqQ")},"data-v-128d4b50",null);a.default=n.exports},yvKl:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("EhQ/"),r=s("xCaS"),i={components:{"m-stage":e.default,"m-card":r.default},name:"fetch",props:["stat","bubble","stall","ins","operation","predPC"]},l={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("v-tooltip",{attrs:{top:"",disabled:0===t.operation.length}},[s("v-layout",{staticClass:"m-row mx-1  my-1",attrs:{slot:"activator",row:"",wrap:""},slot:"activator"},[s("v-flex",{staticClass:"my-2",attrs:{xs2:"","offset-xs0":""}},[s("m-stage",{attrs:{ins:t.ins,name:"F",stat:t.stat,operation:t.operation,bubble:t.bubble,stall:t.stall}})],1),t._v(" "),s("v-flex",{staticClass:" my-2",attrs:{xs2:"","offset-xs2":""}},[s("m-card",{attrs:{title:"predPC",operation:t.operation,value:t.predPC,bubble:t.bubble,stall:t.stall}})],1)],1),t._v(" "),s("span",[t._l(t.operation,function(a){return s("div",{staticClass:"m-operation"},[t._v("\n          "+t._s(a)+"\n      ")])})],2)],1)},staticRenderFns:[]},n=s("VU/8")(i,l,!1,function(t){s("JgHD")},"data-v-f1d820d6",null);a.default=n.exports}});
//# sourceMappingURL=1.3557d4854dee362d8463.js.map