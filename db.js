import mysql from 'mysql2/promise';

//Modify the connection details to match the details specified while
//deploying the SingleStore workspace:
const HOST = '52.71.220.101';
const USER = 'admin';
const PASSWORD = 'Bro123@bruh';
const DATABASE = 'SERENDIPITY1';

// main is run at the end
async function main() {
    let singleStoreConnection;
    try {
        singleStoreConnection = await mysql.createConnection({
        host: HOST,
        user: USER,
        password: PASSWORD,
        database: DATABASE
        }); 
  
        console.log("You have successfully connected to SingleStore.");
    } catch (err) { 
        console.error('ERROR', err);
        process.exit(1);
    } finally {
        if (singleStoreConnection) {
            await singleStoreConnection.end();
        }
    }
}





main();