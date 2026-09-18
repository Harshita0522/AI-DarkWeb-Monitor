def generate_alert(threat):

    if threat['risk_level'] == 'HIGH':

        print('\n===============================')
        print('AI THREAT ALERT GENERATED')
        print('===============================')

        print(f"Threat Type : {threat['category']}")
        print(f"Risk Level  : {threat['risk_level']}")
        print(f"Confidence  : {threat['confidence']}")
        print(f"Content     : {threat['content']}")

        print('===============================\n')