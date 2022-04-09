#!/bin/sh


# LOG_INI_TLP=$(grep "LOG_INI_TLP" env/.env.dev | cut -d = -f 2 | xargs -I{} echo {})
# LOG_INI=$(grep "CONT_LOG_INI" env/.env.dev | cut -d = -f 2 | xargs -I{} echo {})


envsubst < $LOG_INI_TLP > $CONT_LOG_INI
echo "envsubst < $LOG_INI_TLP > $CONT_LOG_INI"

