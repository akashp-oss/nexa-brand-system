// node render_textures.js <out dir> : renders textures.html into JPEGs (needs playwright)
const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+path.resolve(__dirname,'textures.html'));
 const out=await p.evaluate(()=>window.render());for(const k in out){fs.writeFileSync(path.join(process.argv[2],'tex-'+k+'.jpg'),Buffer.from(out[k].split(',')[1],'base64'))}
 await b.close();console.log(Object.keys(out).join(' '))})();
