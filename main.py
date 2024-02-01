from flask import Flask, render_template, request, redirect, jsonify, session




# Load data from the Excel file
file_path = r"C:\inetpub\wwwroot\chatbot_RIDB_contents\RPM Portfolio_L7_new1.xlsx"
df = pd.read_excel(file_path)


@app.route('/portfolio', methods=['GET', 'POST'])
def index_port():
    return render_template('RPM_index_91.html')


@app.route('/role')
def role():
    df_role = df['Service'].unique().tolist()
    df_role = {"answer": df_role, "list_name": "role", "color": "column-1"}
    print(df_role)
    return jsonify(df_role)


@app.route('/scope', methods=["POST"])
def scope():
    df_scope = []
    if request.json.get('scope'):
        name = request.json.get('name')
        list_name = request.json.get('name')
        scope = request.json.get('scope')

        if (len(list_name.split(',  ')) == 1):
            df_scope = df[df['Service'] == scope]
            df_scope = df_scope['Sub Stream'].unique().tolist()
            df_scope = {"answer": df_scope, "list_name": "role,  {}".format(scope), "color": "column-2"}
            return df_scope

        elif (len(list_name.split(',  ')) == 2):
            name = name + ',  ' + scope
            list_name = list_name.split(',  ')
            print(list_name)
            df_scope = df[(df['Service'] == list_name[1]) & (df['Sub Stream'] == scope)]
            df_scope = df_scope['Role'].unique().tolist()
            df_scope = {"answer": df_scope, "list_name": name, "color": "column-3"}
            return df_scope

        elif (len(list_name.split(',  ')) == 3):
            name = name + ',  ' + scope
            list_name = list_name.split(',  ')
            df_scope = df[(df['Service'] == list_name[1]) & (df['Sub Stream'] == list_name[2]) & (df['Role'] == scope)]
            df_scope = df_scope['Scope'].unique().tolist()
            df_scope = {"answer": df_scope, "list_name": name, "color": "column-4"}
            return df_scope

        elif (len(list_name.split(',  ')) == 4):
            name = name + ',  ' + scope
            list_name = list_name.split(',  ')
            df_scope = df[
                (df['Service'] == list_name[1]) & (df['Sub Stream'] == list_name[2]) & (df['Role'] == list_name[3]) & (
                            df['Scope'] == scope)]
            df_scope = df_scope['Work Package'].unique().tolist()
            df_scope = {"answer": df_scope, "list_name": name, "color": "column-5"}
            return df_scope

        elif (len(list_name.split(',  ')) == 5):
            name = name + ',  ' + scope
            list_name = list_name.split(',  ')
            df_scope = df[
                (df['Service'] == list_name[1]) & (df['Sub Stream'] == list_name[2]) & (df['Role'] == list_name[3]) & (
                            df['Scope'] == list_name[4]) & (df['Work Package'] == scope)]
            df_scope = df_scope['Activity (L6)'].unique().tolist()
            df_scope = {"answer": df_scope, "list_name": name, "color": "column-6"}
            return df_scope

        elif (len(list_name.split(',  ')) == 6):
            name = name + ',  ' + scope
            list_name = list_name.split(',  ')
            df_scope = df[
                (df['Service'] == list_name[1]) & (df['Sub Stream'] == list_name[2]) & (df['Role'] == list_name[3]) & (
                            df['Scope'] == list_name[4]) & (df['Work Package'] == list_name[5]) & (
                            df['Activity (L6)'] == scope)]

            work_station = df_scope['Work Instruction (L7)'].tolist()
            work_effort = df_scope['Standard Effort ( In Mins)'].tolist()

            for i in range(len(work_station)):
                work_station[i] = work_station[i] + ',  ' + "Standard Effort(In Mins) = " + str(work_effort[i])
            df_scope = {"answer": work_station, "list_name": name, "color": "column-7"}
            return df_scope

        elif (len(list_name.split(',  ')) == 7):
            name = name + ',  ' + scope
            list_name = list_name.split(',  ')
            df_scope = df[
                (df['Service'] == list_name[1]) & (df['Sub Stream'] == list_name[2]) & (df['Role'] == list_name[3]) & (
                            df['Scope'] == list_name[4]) & (df['Work Package'] == list_name[5]) & (
                            df['Activity (L6)'] == list_name[6])]

            df_scope = df_scope[df_scope['Work Instruction (L7)'] == scope.split(',  ')[0]]

            core_context = df_scope['Core / Context'].tolist()
            spc_family = df_scope['SPC Family'].tolist()
            # job_architecture = df_scope['Job Architecture - Job Role e.g '].tolist()
            skill_level = df_scope['Skill - Level  ( L1, L2, L3, L4)'].tolist()
            delivery_model = df_scope['Delivery Model ( Local / Remote)'].tolist()
            # new_list = [core_context, spc_family, job_architecture, skill_level, delivery_model]
            new_list = [core_context, spc_family, skill_level, delivery_model]
            print(new_list)
            return {"answer": new_list, "list_name": "Table"}

    return df_scope


if __name__ == '__main__':
    app.run(debug=True, port=5016)
