

class Manager:
    navmesh_ref = None
    def __init__(self):
        pass

    @classmethod
    def update_navmesh_ref(cls, navmesh):
        cls.navmesh_ref = navmesh