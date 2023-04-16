const express = require("express");
const app = express();
const router = require("./routes/routes")
const cors = require("cors")


app.use(express.urlencoded({extended: false}));
app.use(express.json());
app.use(cors({origin:true}));

const port = 5000;

app.use("/",router);

app.listen(port, () => {
    console.log(`Server started at ${port}`);
})

