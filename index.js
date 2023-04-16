const express = require("express");
const app = express();
const router = require("./routes/routes")
const cors = require("cors")


app.use(express.urlencoded({extended: false}));
app.use(express.json());
app.use(cors({origin:true}));

if (process.env.NODE_ENV === 'development') {
    app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
  }
  
  if (process.env.NODE_ENV === 'production') {
    app.use(express.errorHandler());
  }

const port = 5000;

app.use("/",router);

app.listen(port, () => {
    console.log(`Server started at ${port}`);
})

