import sd


def get_graph_uuid():
    """
        Returns a UUID that includes to 
        package's UUID to ensure no collisions 
        happen in saving configs
    """
    app = sd.getContext().getSDApplication() 
    uiMgr = app.getQtForPythonUIMgr() 
    graph = uiMgr.getCurrentGraph() 

    graph_uuid = graph.getUID()
    pkg_uuid = graph.getPackage().getUID().strip("{").rstrip("}")

    return f"{pkg_uuid}-{graph_uuid}"