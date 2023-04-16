const router = require("express").Router();
const {GetResponse} = require('../controllers/controllers');

router.post("/api",GetResponse);

module.exports = router;