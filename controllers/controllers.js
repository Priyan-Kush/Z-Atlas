const data = require("../dummy");
const axios = require("axios");

const GetResponse = async(req,res) => {
    try {
        const source = req.body.source;
        const destination = req.body.destination;
        //console.log(req.body);
        let src,dest,route;
         await axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${source}&key=dd5aca3fa0b749c1a62a35db921195fe&language=en&pretty=1`)
         .then((res)=>{
             //console.log(res.data.results[0].geometry);
             src = [res.data.results[0].geometry.lat, res.data.results[0].geometry.lng];
         })

         await axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${destination}&key=dd5aca3fa0b749c1a62a35db921195fe&language=en&pretty=1`)
         .then((res)=>{
             //console.log(res.data.results[0].geometry);
             dest = [res.data.results[0].geometry.lat, res.data.results[0].geometry.lng];
         })

        //   await axios.get('http://7769-2409-4072-783-6cc5-ec2e-8e88-e899-1e55.ngrok.io',{
        //      source:src,
        //      destination:dest
        //   })
        //   .then((res)=>{
        //      route = res.data;
        // })
        //  console.log(route);
        //  let path = [];

        //  route.map((e)=>{
        //      path.push([e.latitude,e.longitude]);
        //  })

        //  console.log(path);

         const da = {
             source: src,
             destination: dest,
             path: data.path
         }

        //console.log(data);
        res.status(200).json({data: da});
    } catch (error) {
        res.status(400).json({message:error});
    }
}

module.exports = {GetResponse}
