#!/bin/bash

cd /code/Quantum_Cryptography_Notes && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token="" &

# Wait for Jupyter to start
sleep 5

echo ""
echo ""
echo "******************************************************************"
echo "******************************************************************"
echo "**                                                              **"
echo "**  QUANTUM CRYPTOGRAPHY ENVIRONMENT IS RUNNING                 **"
echo "**                                                              **"
echo "**  CHECK USAGE INSTRUCTIONS IN DockerSetup.md                  **"
echo "**                                                              **"
echo "**  TO STOP THIS ENVIRONMENT: Press CTRL+C                      **"
echo "**                                                              **"
echo "******************************************************************"
echo "******************************************************************"
echo ""
echo ""

# Keep the script running to see the container logs
wait