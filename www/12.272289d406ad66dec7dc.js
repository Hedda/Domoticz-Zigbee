(window.webpackJsonp=window.webpackJsonp||[]).push([[12],{"7wo0":function(t,n,e){"use strict";e.r(n),e.d(n,"SettingsModule",function(){return x});var c=e("M0ag"),i=e("iInd"),s=e("ey9i"),r=e("H+bZ"),a=e("ntpF"),o=e("8Y7J"),l=e("G0yt"),b=e("s7LF"),d=e("EApP"),u=e("TSSN"),g=e("SVse"),m=e("wTG2");function f(t,n){if(1&t&&(o.Tb(0,"div",4),o.Lc(1,"\n    "),o.Ob(2,"label",5),o.Lc(3,"\n    "),o.Tb(4,"div",6),o.Lc(5,"\n      "),o.Ob(6,"input",7),o.Lc(7,"\n    "),o.Sb(),o.Lc(8,"\n  "),o.Sb()),2&t){const t=o.ic(2);o.Ab(2),o.pc("translate",t.setting.Name)}}function L(t,n){if(1&t&&(o.Tb(0,"div",4),o.Lc(1,"\n    "),o.Ob(2,"label",5),o.Lc(3,"\n    "),o.Tb(4,"div",6),o.Lc(5,"\n      "),o.Ob(6,"input",7),o.Lc(7,"\n    "),o.Sb(),o.Lc(8,"\n  "),o.Sb()),2&t){const t=o.ic(2);o.Ab(2),o.pc("translate",t.setting.Name)}}function p(t,n){if(1&t&&(o.Tb(0,"div",4),o.Lc(1,"\n    "),o.Ob(2,"label",5),o.Lc(3,"\n    "),o.Tb(4,"div",6),o.Lc(5,"\n      "),o.Ob(6,"input",8),o.Lc(7,"\n    "),o.Sb(),o.Lc(8,"\n  "),o.Sb()),2&t){const t=o.ic(2);o.Ab(2),o.pc("translate",t.setting.Name)}}function h(t,n){if(1&t&&(o.Tb(0,"div",4),o.Lc(1,"\n    "),o.Ob(2,"label",5),o.Lc(3,"\n    "),o.Tb(4,"div",6),o.Lc(5,"\n      "),o.Ob(6,"input",9),o.Lc(7,"\n    "),o.Sb(),o.Lc(8,"\n  "),o.Sb()),2&t){const t=o.ic(2);o.Ab(2),o.pc("translate",t.setting.Name)}}function v(t,n){if(1&t&&(o.Tb(0,"div",4),o.Lc(1,"\n    "),o.Ob(2,"label",5),o.Lc(3,"\n    "),o.Tb(4,"div",6),o.Lc(5,"\n      "),o.Tb(6,"ng-select",10),o.Lc(7,"\n      "),o.Sb(),o.Lc(8,"\n    "),o.Sb(),o.Lc(9,"\n  "),o.Sb()),2&t){const t=o.ic(2);o.Ab(2),o.pc("translate",t.setting.Name),o.Ab(4),o.oc("items",t.list)("compareWith",t.compareNumeric)("closeOnSelect",!0)}}function S(t,n){if(1&t&&(o.Tb(0,"div",11),o.Lc(1,"\n    "),o.Ob(2,"input",12),o.Lc(3,"\n    "),o.Ob(4,"label",13),o.Lc(5,"\n  "),o.Sb()),2&t){const t=o.ic(2);o.Ab(2),o.pc("id",t.setting.Name),o.Ab(2),o.pc("for",t.setting.Name),o.pc("translate",t.setting.Name)}}function T(t,n){if(1&t&&(o.Tb(0,"div",1),o.Lc(1,"\n  "),o.Jc(2,f,9,1,"div",2),o.Lc(3,"\n  "),o.Jc(4,L,9,1,"div",2),o.Lc(5,"\n  "),o.Jc(6,p,9,1,"div",2),o.Lc(7,"\n  "),o.Jc(8,h,9,1,"div",2),o.Lc(9,"\n  "),o.Jc(10,v,10,4,"div",2),o.Lc(11,"\n  "),o.Jc(12,S,6,3,"div",3),o.Lc(13,"\n"),o.Sb()),2&t){const t=o.ic();o.oc("formGroupName",t.setting.Name),o.Ab(2),o.oc("ngIf","str"===t.setting.DataType),o.Ab(2),o.oc("ngIf","path"===t.setting.DataType),o.Ab(2),o.oc("ngIf","int"===t.setting.DataType),o.Ab(2),o.oc("ngIf","hex"===t.setting.DataType),o.Ab(2),o.oc("ngIf","list"===t.setting.DataType),o.Ab(2),o.oc("ngIf","bool"===t.setting.DataType)}}new s.c("SettingComponent");let O=(()=>{class t{constructor(t,n,e){this.formBuilder=t,this.fgd=n,this.translate=e,this.list=[]}ngOnChanges(t){let n;if(t.setting&&t.setting.currentValue){this.setting=t.setting.currentValue,"hex"===this.setting.DataType?n=this.formBuilder.group({current:["",b.q.compose([b.q.required,b.q.pattern("^[0-9A-Fa-f]+")])]}):"bool"===this.setting.DataType?n=this.formBuilder.group({current:[]}):"list"===this.setting.DataType?(n=this.formBuilder.group({current:[null,b.q.required]}),this.list=[],this.setting.list.forEach(t=>{const n=Object.keys(t)[0],e=Object.values(t)[0];this.list.push({label:n,value:e})})):n=this.formBuilder.group({current:["",b.q.required]}),this.fgd.form.addControl(this.setting.Name,n);const e=""!==this.setting.current_value?this.setting.current_value:this.setting.default_value;this.fgd.form.get(this.setting.Name).get("current").patchValue(e)}}compareNumeric(t,n){return isNaN(t.value)?t.value===n:t.value===Number(n)}}return t.\u0275fac=function(n){return new(n||t)(o.Nb(b.d),o.Nb(b.f),o.Nb(u.d))},t.\u0275cmp=o.Hb({type:t,selectors:[["app-setting"]],inputs:{setting:"setting",advanced:"advanced"},features:[o.zb([],[{provide:b.b,useExisting:b.f}]),o.yb],decls:2,vars:1,consts:[[3,"formGroupName",4,"ngIf"],[3,"formGroupName"],["class","form-group row mt-2",4,"ngIf"],["class","row mt-2 custom-control custom-checkbox",4,"ngIf"],[1,"form-group","row","mt-2"],["for","current",1,"col-sm-6","col-form-label",3,"translate"],[1,"col-sm"],["type","text","formControlName","current",1,"w-100","form-control"],["type","number","formControlName","current",1,"w-50","form-control"],["type","text","formControlName","current",1,"w-50","form-control"],["bindLabel","label","bindValue","value","formControlName","current",3,"items","compareWith","closeOnSelect"],[1,"row","mt-2","custom-control","custom-checkbox"],["formControlName","current","type","checkbox",1,"custom-control-input","form-control",3,"id"],[1,"ml-3","custom-control-label",3,"for","translate"]],template:function(t,n){1&t&&(o.Jc(0,T,14,7,"div",0),o.Lc(1,"\n")),2&t&&o.oc("ngIf",!1===n.setting.Advanced||n.advanced===n.setting.Advanced)},directives:[g.n,b.l,b.g,u.a,b.c,b.k,b.e,b.o,m.a,b.a],styles:[".custom-control-input.is-valid[_ngcontent-%COMP%] ~ .custom-control-label[_ngcontent-%COMP%], was-validated[_ngcontent-%COMP%]   .custom-control-input[_ngcontent-%COMP%]:valid ~ .custom-control-label[_ngcontent-%COMP%]{color:#000}"]}),t})();const k=["contentRestart"];function y(t,n){if(1&t&&(o.Rb(0),o.Lc(1,"\n                  "),o.Ob(2,"app-setting",28),o.Lc(3,"\n                "),o.Qb()),2&t){const t=n.$implicit,e=o.ic(4);o.Ab(2),o.oc("setting",t)("advanced",e.advanced)}}function N(t,n){if(1&t&&(o.Tb(0,"div",22),o.Lc(1,"\n            "),o.Ob(2,"div",23),o.Lc(3,"\n            "),o.Tb(4,"div",24),o.Lc(5,"\n              "),o.Tb(6,"div",25),o.Lc(7,"\n                "),o.Ob(8,"h5",26),o.Lc(9,"\n              "),o.Sb(),o.Lc(10,"\n              "),o.Tb(11,"div",27),o.Lc(12,"\n                "),o.Jc(13,y,4,2,"ng-container",20),o.Lc(14,"\n              "),o.Sb(),o.Lc(15,"\n            "),o.Sb(),o.Lc(16,"\n          "),o.Sb()),2&t){const t=o.ic().$implicit,n=o.ic(2);o.Ab(2),o.oc("innerHTML",n.getTranslation("setting.header.",t._Theme),o.Cc),o.Ab(6),o.oc("innerHTML",n.getTranslation("setting.subtitle.",t._Theme),o.Cc),o.Ab(5),o.oc("ngForOf",t.ListOfSettings)}}function A(t,n){if(1&t&&(o.Tb(0,"div"),o.Lc(1,"\n          "),o.Jc(2,N,17,3,"div",21),o.Lc(3,"\n        "),o.Sb()),2&t){const t=n.$implicit,e=o.ic(2);o.Ab(2),o.oc("ngIf",e.hasBasicSettings(t.ListOfSettings))}}function w(t,n){if(1&t){const t=o.Ub();o.Tb(0,"form",4),o.Lc(1,"\n  "),o.Tb(2,"fieldset",5),o.Lc(3,"\n    "),o.Tb(4,"legend"),o.Lc(5,"\n      "),o.Tb(6,"div",6),o.Lc(7,"\n        "),o.Ob(8,"div",7),o.jc(9,"translate"),o.Lc(10,"\n        "),o.Tb(11,"div",8),o.Lc(12,"\n          "),o.Tb(13,"div",9),o.Lc(14,"\n            "),o.Tb(15,"div",10),o.Lc(16,"\n              "),o.Tb(17,"button",11),o.ec("click",function(){return o.Bc(t),o.ic().updateSettings()}),o.Sb(),o.Lc(18,"\n            "),o.Sb(),o.Lc(19,"\n            "),o.Tb(20,"div",12),o.Lc(21,"\n              "),o.Tb(22,"button",13),o.ec("click",function(){return o.Bc(t),o.ic().reinitSettings()}),o.Sb(),o.Lc(23,"\n            "),o.Sb(),o.Lc(24,"\n            "),o.Tb(25,"div",14),o.Lc(26,"\n              "),o.Tb(27,"input",15),o.ec("click",function(n){return o.Bc(t),o.ic().advancedSettings(n)}),o.Sb(),o.Lc(28,"\n              "),o.Ob(29,"label",16),o.Lc(30,"\n            "),o.Sb(),o.Lc(31,"\n          "),o.Sb(),o.Lc(32,"\n        "),o.Sb(),o.Lc(33,"\n      "),o.Sb(),o.Lc(34,"\n    "),o.Sb(),o.Lc(35,"\n    "),o.Ob(36,"h5",17),o.jc(37,"translate"),o.Lc(38,"\n  "),o.Sb(),o.Lc(39,"\n  "),o.Tb(40,"div",18),o.Lc(41,"\n    "),o.Tb(42,"div",6),o.Lc(43,"\n      "),o.Tb(44,"div",19),o.Lc(45,"\n        "),o.Jc(46,A,4,1,"div",20),o.Lc(47,"\n      "),o.Sb(),o.Lc(48,"\n    "),o.Sb(),o.Lc(49,"\n  "),o.Sb(),o.Lc(50,"\n"),o.Sb()}if(2&t){const t=o.ic();o.oc("formGroup",t.form),o.Ab(8),o.oc("innerHTML",o.kc(9,6,"setting.help.legend"),o.Cc),o.Ab(9),o.oc("disabled",!t.form.valid),o.Ab(10),o.oc("checked",t.advanced),o.Ab(9),o.oc("innerHTML",o.kc(37,8,"setting.help.link"),o.Cc),o.Ab(10),o.oc("ngForOf",t.settings)}}function C(t,n){1&t&&(o.Lc(0,"\n  "),o.Tb(1,"div",29),o.Lc(2,"\n    "),o.Ob(3,"h4",30),o.Lc(4,"\n    "),o.Tb(5,"button",31),o.ec("click",function(){return n.$implicit.dismiss("Cross click")}),o.Lc(6,"\n      "),o.Tb(7,"span",32),o.Lc(8,"\xd7"),o.Sb(),o.Lc(9,"\n    "),o.Sb(),o.Lc(10,"\n  "),o.Sb(),o.Lc(11,"\n  "),o.Ob(12,"div",33),o.Lc(13,"\n  "),o.Tb(14,"div",34),o.Lc(15,"\n    "),o.Tb(16,"button",35),o.ec("click",function(){return n.$implicit.dismiss("cancel")}),o.Sb(),o.Lc(17,"\n  "),o.Sb(),o.Lc(18,"\n"))}function J(t,n){1&t&&(o.Lc(0,"\n  "),o.Tb(1,"div",29),o.Lc(2,"\n    "),o.Ob(3,"h4",36),o.Lc(4,"\n    "),o.Tb(5,"button",31),o.ec("click",function(){return n.$implicit.dismiss("Cross click")}),o.Lc(6,"\n      "),o.Tb(7,"span",32),o.Lc(8,"\xd7"),o.Sb(),o.Lc(9,"\n    "),o.Sb(),o.Lc(10,"\n  "),o.Sb(),o.Lc(11,"\n  "),o.Ob(12,"div",37),o.Lc(13,"\n  "),o.Tb(14,"div",34),o.Lc(15,"\n    "),o.Tb(16,"button",38),o.ec("click",function(){return n.$implicit.dismiss("cancel")}),o.Sb(),o.Lc(17,"\n  "),o.Sb(),o.Lc(18,"\n"))}function I(t,n){1&t&&(o.Lc(0,"\n  "),o.Tb(1,"div",29),o.Lc(2,"\n    "),o.Ob(3,"h4",39),o.Lc(4,"\n    "),o.Tb(5,"button",31),o.ec("click",function(){return n.$implicit.dismiss("Cross click")}),o.Lc(6,"\n      "),o.Tb(7,"span",32),o.Lc(8,"\xd7"),o.Sb(),o.Lc(9,"\n    "),o.Sb(),o.Lc(10,"\n  "),o.Sb(),o.Lc(11,"\n  "),o.Ob(12,"div",40),o.Lc(13,"\n  "),o.Tb(14,"div",34),o.Lc(15,"\n    "),o.Tb(16,"button",41),o.ec("click",function(){return n.$implicit.dismiss("cancel")}),o.Sb(),o.Lc(17,"\n  "),o.Sb(),o.Lc(18,"\n"))}new s.c("SettingsComponent");const R=[{path:"",component:(()=>{class t{constructor(t,n,e,c,i,s){this.modalService=t,this.apiService=n,this.formBuilder=e,this.toastr=c,this.headerService=i,this.translate=s,this.advanced=!1}ngOnInit(){this.form=this.formBuilder.group({}),this.apiService.getSettings().subscribe(t=>{this.settings=t,this.settings.sort((t,n)=>t._Order-n._Order)})}reinitSettings(){this.settings.forEach(t=>{const n=[];t.ListOfSettings.forEach(t=>{"path"!==t.DataType&&(t.current_value=t.default_value),n.push(Object.assign({},t))}),t.ListOfSettings=n}),this.settings=[...this.settings],this.form.markAsTouched()}advancedSettings(t){this.advanced=!!t.currentTarget.checked}updateSettings(){this.form.invalid?this.form.markAsTouched():(Object.keys(this.form.value).forEach(t=>{!0===this.form.value[t].current?this.form.value[t].current=1:!1===this.form.value[t].current&&(this.form.value[t].current=0)}),this.apiService.putSettings(this.form.value).subscribe(t=>{this.form.markAsPristine(),this.toastr.success(this.translate.instant("api.global.succes.update.title")),this.apiService.getSettings().subscribe(t=>{this.settings=t,this.settings.sort((t,n)=>t._Order-n._Order)}),this.apiService.getRestartNeeded().subscribe(t=>{1===t.RestartNeeded?(this.headerService.setRestart(!0),this.open(this.contentRestart)):2===t.RestartNeeded?this.open(this.contentReset):3===t.RestartNeeded&&this.open(this.contentErase)})}))}open(t){this.modalService.open(t,{ariaLabelledBy:"modal-basic-title"}).result.then(t=>{},t=>{})}hasBasicSettings(t){return!!this.advanced||t.filter(t=>!1===t.Advanced).length>0}getTranslation(t,n){return this.translate.instant(t.concat(n))}}return t.\u0275fac=function(n){return new(n||t)(o.Nb(l.e),o.Nb(r.a),o.Nb(b.d),o.Nb(d.b),o.Nb(a.a),o.Nb(u.d))},t.\u0275cmp=o.Hb({type:t,selectors:[["app-settings"]],viewQuery:function(t,n){var e;1&t&&(o.Rc(k,!0),o.Rc(k,!0),o.Rc(k,!0)),2&t&&(o.xc(e=o.fc())&&(n.contentRestart=e.first),o.xc(e=o.fc())&&(n.contentReset=e.first),o.xc(e=o.fc())&&(n.contentErase=e.first))},decls:11,vars:1,consts:[[3,"formGroup",4,"ngIf"],["contentRestart",""],["contentReset",""],["contentErase",""],[3,"formGroup"],[1,"h-100"],[1,"row"],[1,"col-sm-8",3,"innerHTML"],[1,"col-sm-4"],[1,"d-flex","flex-row-reverse","align-items-center"],[1,"p-2"],["translate","setting.validate.button",1,"btn","btn-primary",3,"disabled","click"],[1,"p-2","ml-3"],["translate","setting.reinit.button",1,"btn","btn-secondary",3,"click"],[1,"switch","switch-sm"],["type","checkbox","id","switch-advanced",1,"switch",3,"checked","click"],["for","switch-advanced","translate","setting.advanced.button",1,"mb-0"],[1,"card-title",3,"innerHTML"],[1,"mt-3"],[1,"col-sm-12","card-columns"],[4,"ngFor","ngForOf"],["class","card",4,"ngIf"],[1,"card"],[1,"card-header",3,"innerHTML"],[1,"card-body"],[1,"card-title"],[3,"innerHTML"],[1,"card-text"],[3,"setting","advanced"],[1,"modal-header"],["id","modal-basic-title","translate","setting.reloadplugin.alert.title",1,"modal-title"],["type","button","aria-label","Close",1,"close",3,"click"],["aria-hidden","true"],["translate","setting.reloadplugin.alert.subject",1,"modal-body"],[1,"modal-footer"],["type","button","translate","setting.reloadplugin.alert.cancel",1,"btn","btn-outline-dark",3,"click"],["id","modal-basic-title","translate","setting.resetplugin.alert.title",1,"modal-title"],["translate","setting.resetplugin.alert.subject",1,"modal-body"],["type","button","translate","setting.resetplugin.alert.cancel",1,"btn","btn-outline-dark",3,"click"],["id","modal-basic-title","translate","setting.eraseplugin.alert.title",1,"modal-title"],["translate","setting.eraseplugin.alert.subject",1,"modal-body"],["type","button","translate","setting.eraseplugin.alert.cancel",1,"btn","btn-outline-dark",3,"click"]],template:function(t,n){1&t&&(o.Jc(0,w,51,10,"form",0),o.Lc(1,"\n\n"),o.Jc(2,C,19,0,"ng-template",null,1,o.Kc),o.Lc(4,"\n\n"),o.Jc(5,J,19,0,"ng-template",null,2,o.Kc),o.Lc(7,"\n\n"),o.Jc(8,I,19,0,"ng-template",null,3,o.Kc),o.Lc(10,"\n")),2&t&&o.oc("ngIf",n.settings)},directives:[g.n,b.s,b.l,b.f,u.a,g.m,O],pipes:[u.c],styles:[""]}),t})(),data:{title:Object(s.d)("settings")}}];let _=(()=>{class t{}return t.\u0275mod=o.Lb({type:t}),t.\u0275inj=o.Kb({factory:function(n){return new(n||t)},providers:[],imports:[[i.i.forChild(R)],i.i]}),t})(),x=(()=>{class t{}return t.\u0275mod=o.Lb({type:t}),t.\u0275inj=o.Kb({factory:function(n){return new(n||t)},imports:[[_,c.a]]}),t})()}}]);