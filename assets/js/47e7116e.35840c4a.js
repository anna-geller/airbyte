"use strict";(self.webpackChunkdocu=self.webpackChunkdocu||[]).push([[30921],{42945:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>l,toc:()=>p});var a=n(87462),r=(n(67294),n(3905));const i={},o="SFTP JSON",l={unversionedId:"integrations/destinations/sftp-json",id:"integrations/destinations/sftp-json",title:"SFTP JSON",description:"Overview",source:"@site/../docs/integrations/destinations/sftp-json.md",sourceDirName:"integrations/destinations",slug:"/integrations/destinations/sftp-json",permalink:"/integrations/destinations/sftp-json",draft:!1,editUrl:"https://github.com/airbytehq/airbyte/blob/master/docs/../docs/integrations/destinations/sftp-json.md",tags:[],version:"current",frontMatter:{},sidebar:"mySidebar",previous:{title:"SelectDB",permalink:"/integrations/destinations/selectdb"},next:{title:"Snowflake",permalink:"/integrations/destinations/snowflake"}},s={},p=[{value:"Overview",id:"overview",level:2},{value:"Sync Overview",id:"sync-overview",level:3},{value:"Output schema",id:"output-schema",level:4},{value:"Features",id:"features",level:4},{value:"Performance considerations",id:"performance-considerations",level:4},{value:"Getting Started",id:"getting-started",level:2},{value:"Example:",id:"example",level:3},{value:"Changelog",id:"changelog",level:2}],c={toc:p},d="wrapper";function u(e){let{components:t,...n}=e;return(0,r.kt)(d,(0,a.Z)({},c,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"sftp-json"},"SFTP JSON"),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"This destination writes data to a directory on an SFTP server."),(0,r.kt)("h3",{id:"sync-overview"},"Sync Overview"),(0,r.kt)("h4",{id:"output-schema"},"Output schema"),(0,r.kt)("p",null,"Each stream will be output into its own file.\nEach file will contain a collection of ",(0,r.kt)("inlineCode",{parentName:"p"},"json")," objects which correspond directly with the data supplied by the source."),(0,r.kt)("h4",{id:"features"},"Features"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:"left"},"Feature"),(0,r.kt)("th",{parentName:"tr",align:"left"},"Supported"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:"left"},"Full Refresh Sync"),(0,r.kt)("td",{parentName:"tr",align:"left"},"Yes")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:"left"},"Incremental - Append Sync"),(0,r.kt)("td",{parentName:"tr",align:"left"},"Yes")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:"left"},"Namespaces"),(0,r.kt)("td",{parentName:"tr",align:"left"},"No")))),(0,r.kt)("h4",{id:"performance-considerations"},"Performance considerations"),(0,r.kt)("p",null,"This integration will be constrained by the connection speed to the SFTP server and speed at which that server accepts writes."),(0,r.kt)("h2",{id:"getting-started"},"Getting Started"),(0,r.kt)("p",null,"The ",(0,r.kt)("inlineCode",{parentName:"p"},"destination_path")," can refer to any path that the associated account has write permissions to."),(0,r.kt)("p",null,"The ",(0,r.kt)("inlineCode",{parentName:"p"},"filename")," ",(0,r.kt)("strong",{parentName:"p"},"should not")," have an extension in the configuration, as ",(0,r.kt)("inlineCode",{parentName:"p"},".jsonl")," will be added on by the connector."),(0,r.kt)("h3",{id:"example"},"Example:"),(0,r.kt)("p",null,"If ",(0,r.kt)("inlineCode",{parentName:"p"},"destination_path")," is set to ",(0,r.kt)("inlineCode",{parentName:"p"},"/myfolder/files")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"filename")," is set to ",(0,r.kt)("inlineCode",{parentName:"p"},"mydata"),", the resulting file will be ",(0,r.kt)("inlineCode",{parentName:"p"},"/myfolder/files/mydata.jsonl"),"."),(0,r.kt)("p",null,"These files can then be accessed by creating an SFTP connection to the server and navigating to the ",(0,r.kt)("inlineCode",{parentName:"p"},"destination_path"),"."),(0,r.kt)("h2",{id:"changelog"},"Changelog"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:"left"},"Version"),(0,r.kt)("th",{parentName:"tr",align:"left"},"Date"),(0,r.kt)("th",{parentName:"tr",align:"left"},"Pull Request"),(0,r.kt)("th",{parentName:"tr",align:"left"},"Subject"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:"left"},"0.1.0"),(0,r.kt)("td",{parentName:"tr",align:"left"},"2022-11-24"),(0,r.kt)("td",{parentName:"tr",align:"left"},(0,r.kt)("a",{parentName:"td",href:"https://github.com/airbytehq/airbyte/pull/4924"},"4924")),(0,r.kt)("td",{parentName:"tr",align:"left"},"\ud83c\udf89 New Destination: SFTP JSON")))))}u.isMDXComponent=!0},3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>f});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var s=a.createContext({}),p=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},c=function(e){var t=p(e.components);return a.createElement(s.Provider,{value:t},e.children)},d="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),d=p(n),m=r,f=d["".concat(s,".").concat(m)]||d[m]||u[m]||i;return n?a.createElement(f,o(o({ref:t},c),{},{components:n})):a.createElement(f,o({ref:t},c))}));function f(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,o=new Array(i);o[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[d]="string"==typeof e?e:r,o[1]=l;for(var p=2;p<i;p++)o[p]=n[p];return a.createElement.apply(null,o)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"}}]);