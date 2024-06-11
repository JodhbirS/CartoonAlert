const { exec } = require('child_process');

export default function handler(req, res) {
  const authHeader = req.headers.get('authorization');
  if (
    !process.env.CRON_SECRET ||
    authHeader !== `Bearer ${process.env.CRON_SECRET}`
  ) {
    return res.status(401).json({ success: false, message: 'Unauthorized' });
  }

  exec('python3 api/cron.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing script: ${error.message}`);
      return res.status(500).json({ success: false, message: 'Internal Server Error' });
    }
    if (stderr) {
      console.error(`Script stderr: ${stderr}`);
      return res.status(500).json({ success: false, message: 'Internal Server Error' });
    }
    console.log(`Script stdout: ${stdout}`);
    res.status(200).json({ success: true, message: 'Cron job executed successfully' });
  });
}
